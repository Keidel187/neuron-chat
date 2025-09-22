import customtkinter as ctk
import ctypes
from ui.main_window import MainWindow

APP_USER_MODEL_ID = '55'  # Windows App User Model ID for taskbar grouping, notifications, etc.
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_USER_MODEL_ID)

# Inherit from MainWindow to create the main application class
class Main(MainWindow):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = Main()
    app.mainloop()