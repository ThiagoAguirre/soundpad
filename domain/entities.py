# Definição da entidade Soundf

from dataclasses import dataclass
from pathlib import Path

@dataclass
class SoundFile:
    name: str
    file_path: Path
    keybind: str