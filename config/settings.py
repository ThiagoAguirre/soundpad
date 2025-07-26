# Configurações (pastas, atalhos, volume)

from pathlib import Path
from domain.entities import SoundFile

BASE_DIR = Path(__file__).resolve().parent.parent
SOUNDS_DIR = BASE_DIR / 'assets' / 'sounds'

SOUND_LIST = [
    SoundFile(name="Laugh", file_path=SOUNDS_DIR / "tf_nemesis.mp3", keybind="num 1"),
    SoundFile(name="Applause", file_path=SOUNDS_DIR / "applause.wav", keybind="num 2"),
    SoundFile(name="Boo", file_path=SOUNDS_DIR / "boo.wav", keybind="num 3"),
]