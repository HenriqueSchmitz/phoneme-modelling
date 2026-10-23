from pathlib import Path
from typing import Optional

from pydantic import BaseModel



class GeminiConfig(BaseModel):
    project: str
    model: str
    location: str
    voices: list[str]
    live: bool = False
    ref_dir: Optional[Path] = None
    ref_mode: str = "ref"
    prompts_file: Optional[Path] = None
