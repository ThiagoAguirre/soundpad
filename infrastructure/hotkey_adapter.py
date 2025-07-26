# infrastructure/hotkey_adapter.py

import keyboard
from infrastructure.sound_adapter import play_sound

def register_hotkeys(sounds):
    for sound in sounds:
        keyboard.add_hotkey(sound.keybind, lambda path=sound.file_path: play_sound(path))
