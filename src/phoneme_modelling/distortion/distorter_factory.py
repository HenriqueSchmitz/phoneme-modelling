from typing import Any, Optional, Type

from pydantic import BaseModel

from phoneme_modelling.distortion.distorter import AudioDistorter


class AudioDistorterFactory:
    def __init__(self) -> None:
        self._registry: list[tuple[Type[AudioDistorter], Optional[Type[BaseModel]]]] = []

    def register(self, distorter_cls: Type[AudioDistorter], config_cls: Optional[Type[BaseModel]] = None) -> None:
        """Register a distorter class along with its corresponding Pydantic config class."""
        self._registry.append((distorter_cls, config_cls))

    def generate(self, distortions: dict[str, Any]) -> list[AudioDistorter]:
        distorters: list[AudioDistorter] = []
        for distorter_cls, config_cls in self._registry:
            distortion_name = distorter_cls.get_name()
            if distortion_name in distortions:
                if config_cls is not None:
                    config_instance = config_cls(**distortions[distortion_name])
                    distorters.append(distorter_cls(config_instance))
                else:
                    distorters.append(distorter_cls())
        return distorters