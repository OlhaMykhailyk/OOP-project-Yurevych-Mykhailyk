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

    def start_game(self):
        self.start_frame.destroy()
        self.create_board()

    def create_board(self):
        self.canvas = tk.Canvas(self.root, width=CELL_SIZE * BOARD_SIZE, height=CELL_SIZE * BOARD_SIZE)
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        green = "#626F47"
        light_green = "#F5ECD5"

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                color = light_green if (row + col) % 2 == 0 else green
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = CheckersApp(root)
    root.mainloop()
