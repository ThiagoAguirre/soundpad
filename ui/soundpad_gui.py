import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import os
import threading

class SoundPadApp:
    def __init__(self, master, sound_files, sound_folder):
        self.master = master
        self.sound_files = sound_files
        self.sound_folder = sound_folder
        self.assigned_pads = {}

        self.pad_buttons = []
        self.file_listbox = None

        self.setup_gui()

    def setup_gui(self):
        self.master.title("SoundPad")

        # Lista de arquivos
        tk.Label(self.master, text="Arquivos disponíveis:").pack()
        self.file_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, width=50)
        for f in self.sound_files:
            self.file_listbox.insert(tk.END, f)
        self.file_listbox.pack(pady=5)

        # Botão para criar pad
        tk.Button(self.master, text="Atribuir a um novo pad", command=self.assign_to_pad).pack(pady=5)

        # Área dos pads
        self.pad_frame = tk.Frame(self.master)
        self.pad_frame.pack(pady=10)

    def assign_to_pad(self):
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione um arquivo primeiro.")
            return

        filename = self.file_listbox.get(selection[0])
        pad_index = len(self.pad_buttons) + 1

        btn = tk.Button(self.pad_frame, text=f"Pad {pad_index}: {filename}", width=30,
                        command=lambda: self.play_sound_thread(filename))
        btn.pack(pady=2)
        self.pad_buttons.append(btn)
        self.assigned_pads[pad_index] = filename

    def play_sound_thread(self, filename):
        # Reproduz o som em uma thread separada para não travar o tkinter
        thread = threading.Thread(target=self.play_sound, args=(filename,))
        thread.start()

    def play_sound(self, filename):
        try:
            filepath = os.path.join(self.sound_folder, filename)
            playsound(filepath)
        except Exception as e:
            messagebox.showerror("Erro ao tocar o som", str(e))

def start_gui(sound_files, sound_folder):
    root = tk.Tk()
    app = SoundPadApp(root, sound_files, sound_folder)
    root.mainloop()
