import tkinter as tk

CELL_SIZE = 60
BOARD_SIZE = 8

class CheckersApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Гра в шашки")
        self.selected_piece = None
        self.pieces = {}
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
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
        self.place_pieces()

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
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def place_pieces(self):
        for row in range(3):
            for col in range(BOARD_SIZE):
                if (row + col) % 2 != 0:
                    self.create_piece(row, col, "black")

        for row in range(5, 8):
            for col in range(BOARD_SIZE):
                if (row + col) % 2 != 0:
                    self.create_piece(row, col, "white")

    def create_piece(self, row, col, color):
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        piece = self.canvas.create_oval(
            x - 20, y - 20, x + 20, y + 20,
            fill=color, outline="gray"
        )
        self.pieces[piece] = (row, col, color)

    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        clicked_piece = self.get_piece_at(row, col)

        if self.selected_piece:
            if not clicked_piece:
                self.move_piece(self.selected_piece, row, col)
                self.selected_piece = None
        elif clicked_piece:
            self.selected_piece = clicked_piece

    def get_piece_at(self, row, col):
        for piece_id, (r, c, _) in self.pieces.items():
            if r == row and c == col:
                return piece_id
        return None

    def move_piece(self, piece_id, new_row, new_col):
        x = new_col * CELL_SIZE + CELL_SIZE // 2
        y = new_row * CELL_SIZE + CELL_SIZE // 2
        self.canvas.coords(piece_id, x - 20, y - 20, x + 20, y + 20)
        _, _, color = self.pieces[piece_id]
        self.pieces[piece_id] = (new_row, new_col, color)

if __name__ == "__main__":
    root = tk.Tk()
    app = CheckersApp(root)
    root.mainloop()
