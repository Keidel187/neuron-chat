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

        self.manager = AIManager()
        user_input = "Hello this is a Test"

        # Try to generate text using the AIManager if not print RuntimeError
        try:
            text = self.manager.generate_text(user_input)
            print(f"AI response: {text}")
        except RuntimeError as error:
            print(f"AI generation failed: {error}")

if __name__ == "__main__":
    app = Main()
    app.mainloop()