# infrastructure/sound_adapter.py

import sounddevice as sd
import soundfile as sf

def play_sound(file_path):
    data, fs = sf.read(file_path, dtype='float32')
    sd.play(data, fs)
