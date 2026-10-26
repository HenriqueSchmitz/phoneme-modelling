from typing import Optional

from pydantic import BaseModel




class PhonemeDistortionRequest(BaseModel):
    from_phoneme: str
    to_phoneme: str
    distortion_intensities: Optional[list[float]] = None
    min_distortion_intensity: Optional[float] = None
    max_distortion_intensity: Optional[float] = None
    number_of_samples: Optional[int] = None