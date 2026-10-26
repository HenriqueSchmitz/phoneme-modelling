from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from phoneme_modelling.schema.phoneme_evaluation import PhonemeEvaluation



class AudioEvaluator(ABC):

    def __init__(self, config: Optional[BaseModel] = None):
        pass

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        raise NotImplementedError()

    @abstractmethod
    def evaluate(self, target_phoneme: str, target_phoneme_ipa: str, audio_path: Path) -> PhonemeEvaluation:
        raise NotImplementedError()
    