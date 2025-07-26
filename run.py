from ui.soundpad_gui import start_gui
import os

# Caminho para a pasta onde estão os áudios
SOUND_FOLDER = os.path.join("assets", "sounds")

# Detecta arquivos de áudio válidos na pasta
def detect_sound_files(folder):
    valid_ext = ('.mp3', '.wav')
    return [f for f in os.listdir(folder) if f.lower().endswith(valid_ext)]

if __name__ == "__main__":
    sound_files = detect_sound_files(SOUND_FOLDER)
    start_gui(sound_files, SOUND_FOLDER)
