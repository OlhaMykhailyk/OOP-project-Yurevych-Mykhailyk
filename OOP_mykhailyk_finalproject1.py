import tkinter as tk

CELL_SIZE = 60
BOARD_SIZE = 8

class CheckersApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Гра в шашки")
        self.create_start_screen()

    def create_start_screen(self):
        pastel = "#F5ECD5"
        button_green = "#A4B465"

        self.start_frame = tk.Frame(self.root, bg=pastel, padx=50, pady=50)
        self.start_frame.pack()

        tk.Label(self.start_frame, text="Шашки", font=("Georgia", 24), bg=pastel).pack(pady=20)

        tk.Button(self.start_frame, text="Почати", font=("Helvetica", 16), width=15,
                  bg=button_green, fg="white", activebackground="#FF85B3",
                  command=self.start_game).pack(pady=10)

        tk.Button(self.start_frame, text="Вийти", font=("Helvetica", 16), width=15,
                  bg=button_green, fg="white", activebackground="#FF85B3",
                  command=self.root.quit).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CheckersApp(root)
    root.mainloop()
