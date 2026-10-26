from typing import Any

import pandas as pd
from pandas import DataFrame
from pathlib import Path

from phoneme_modelling.evaluation.evaluators.debug import DebugEvaluator
from phoneme_modelling.evaluation.evaluator import AudioEvaluator
from phoneme_modelling.evaluation.evaluator_factory import AudioEvaluatorFactory
from phoneme_modelling.schema.phoneme_evaluation import PhonemeEvaluationOutput
from phoneme_modelling.schema.phoneme_pipeline_config import PhonemePipelineConfig
from phoneme_modelling.schema.synthetic_phoneme_metadata import SyntheticPhonemeMetadata


class AudioEvaluationPipeline():

    @staticmethod
    def build_evaluators(configs: dict[str, Any]) -> list[AudioEvaluator]:
        factory = AudioEvaluatorFactory()
        factory.register(DebugEvaluator, None)
        return factory.generate(configs)

    @classmethod
    def run(
        cls,
        pipeline_config: PhonemePipelineConfig,
        audio_metadata_file_path: Path,
        evaluation_output_path: Path,
    ) -> None:
        evaluation_output: list[PhonemeEvaluationOutput] = []
        evaluator_configs = pipeline_config.evaluator_configs
        if evaluator_configs is None:
            return
        evaluators = cls.build_evaluators(evaluator_configs)
        audio_metadata: list[dict] = pd.read_csv(audio_metadata_file_path).to_dict(orient="records")
        for audio_dict in audio_metadata:
            audio_info = SyntheticPhonemeMetadata.model_validate(audio_dict)
            for evaluator in evaluators:
                result = evaluator.evaluate(
                    target_phoneme=audio_info.actual_phoneme_text,
                    target_phoneme_ipa=audio_info.actual_phoneme_ipa,
                    audio_path=Path(audio_info.file_path)
                )
                output = PhonemeEvaluationOutput(
                    evaluation=evaluator.get_name(),
                    **audio_info.model_dump(),
                    **result.model_dump())
                evaluation_output.append(output)
        DataFrame([entry.model_dump() for entry in evaluation_output]).to_csv(evaluation_output_path, index=False)
