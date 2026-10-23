from typing import TypedDict, Optional, Any

class PhonemeDistortionRequest(TypedDict):
    from_phoneme: str
    to_phoneme: str
    distortion_intensities: Optional[list[float]]
    min_distortion_intensity: Optional[float]
    max_distortion_intensity: Optional[float]
    number_of_samples: Optional[int]

class PhonemeGenerationRequests(TypedDict):
    number_of_digits: int
    phonemes_to_generate: list[str]
    distortions_to_generate: Optional[list[PhonemeDistortionRequest]]
    generator_configs: dict[str, Any]