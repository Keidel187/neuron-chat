import customtkinter as ctk
import ctypes
import os
from components.locate_assets import asset_path

APP_USER_MODEL_ID = '55'  # Windows App User Model ID for taskbar grouping, notifications, etc.
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_USER_MODEL_ID)

WINDOW_SIZE = "600x500"

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(WINDOW_SIZE)
        self.title("NeuronChat")

        icon_file = asset_path("neuron-chat.ico")
        if os.path.exists(icon_file):
            try:
                self.iconbitmap(icon_file)
            except Exception:
                print("Error: Failed to set window icon.")
                pass

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()