from typing import Any, Optional, Type

from pydantic import BaseModel

from phoneme_modelling.evaluation.evaluator import AudioEvaluator


class AudioEvaluatorFactory:
    def __init__(self) -> None:
        self._registry: list[tuple[Type[AudioEvaluator], Optional[Type[BaseModel]]]] = []

    def register(self, evaluator_cls: Type[AudioEvaluator], config_cls: Optional[Type[BaseModel]] = None) -> None:
        """Register an evaluator class."""
        self._registry.append((evaluator_cls, config_cls))

    def generate(self, evaluations: dict[str, Any]) -> list[AudioEvaluator]:
        evaluators: list[AudioEvaluator] = []
        for evaluator_cls, config_cls in self._registry:
            evaluation_name = evaluator_cls.get_name()
            if evaluation_name in evaluations:
                if config_cls is not None:
                    config_instance = config_cls(**evaluations[evaluation_name])
                    evaluators.append(evaluator_cls(config_instance))
                else:
                    evaluators.append(evaluator_cls())
        return evaluators