import customtkinter as ctk

WINDOW_SIZE = "600x500"

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(WINDOW_SIZE)
        self.title("Test")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()