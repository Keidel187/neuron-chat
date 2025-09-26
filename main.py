import customtkinter as ctk
import ctypes
from ui.main_window import MainWindow
from ai.ai_manager import AIManager

APP_USER_MODEL_ID = '55'  # Windows App User Model ID for taskbar grouping, notifications, etc.
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_USER_MODEL_ID)

# Inherit from MainWindow to create the main application class
class Main(MainWindow):
    def __init__(self):
        super().__init__()

    def main_test(self):
        ai = AIManager()
        user_input = "Hello, my name is"
        output = ai.generate_text(user_input)
        print(f"AI Output: {output}")

if __name__ == "__main__":
    app = Main()
    app.main_test() # TODO: remove this later
    app.mainloop()