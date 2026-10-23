from typing import Any, Optional, Type

from pydantic import BaseModel

from phoneme_modelling.synthetic_audio.generation import SyntheticAudioGenerator


class SyntheticAudioGeneratorFactory:
    def __init__(self) -> None:
        self._registry: list[tuple[Type[SyntheticAudioGenerator], Optional[Type[BaseModel]]]] = []

    def register(self, generator_cls: Type[SyntheticAudioGenerator], config_cls: Optional[Type[BaseModel]] = None) -> None:
        """Register a generator class along with its corresponding Pydantic config class."""
        self._registry.append((generator_cls, config_cls))

    def generate(self, configs: dict[str, Any]) -> list[SyntheticAudioGenerator]:
        generators: list[SyntheticAudioGenerator] = []
        for generator_cls, config_cls in self._registry:
            config_name = generator_cls.get_config_name()
            if config_name in configs:
                if config_cls is not None:
                    config_instance = config_cls(**configs[config_name])
                    generators.append(generator_cls(config_instance))
                else:
                    generators.append(generator_cls())
        return generators