from pathlib import Path

from phoneme_modelling.evaluation.evaluator import AudioEvaluator
from phoneme_modelling.schema.phoneme_evaluation import PhonemeEvaluation



class DebugEvaluator(AudioEvaluator):

    @staticmethod
    def get_name() -> str:
        return "debug"

    def evaluate(self, target_phoneme: str, target_phoneme_ipa: str, audio_path: Path) -> PhonemeEvaluation:
        debug_text = (
            f"Running debug evaluator for target_phoneme: {target_phoneme}, target_phoneme_ipa: "
            f"{target_phoneme_ipa}, audio_path: {audio_path}"
        )
        print(debug_text)
        return PhonemeEvaluation(
            is_correct=True,
            detected_phoneme_text=target_phoneme,
            detected_phoneme_ipa=target_phoneme_ipa,
            quality=0.9
        )