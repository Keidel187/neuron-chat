import customtkinter as ctk
import os
from .components.locate_assets import asset_path

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

        self.grid_columnconfigure([0, 1, 2, 3, 4], weight=1)
        self.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)

        self.test_button = ctk.CTkButton(self, text="Test Button", command=self.button_pressed)
        self.test_button.grid(column=2, row=3, padx=10, pady=5, sticky="nsew")

    def button_pressed(self):
        print("Button has been pressed!")