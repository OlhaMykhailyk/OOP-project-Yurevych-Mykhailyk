import tkinter as tk

CELL_SIZE = 60
BOARD_SIZE = 8

class CheckersApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Гра в шашки")
        self.selected_piece = None
        self.pieces = {}
        self.turn = "white"
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
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.turn_label = tk.Label(self.board_frame, text="Хід білих", font=("Helvetica", 16))
        self.turn_label.pack(pady=10)

        self.canvas = tk.Canvas(self.board_frame, width=CELL_SIZE * BOARD_SIZE, height=CELL_SIZE * BOARD_SIZE)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
        self.place_pieces()

        quit_button = tk.Button(self.board_frame, text="Завершити гру", font=("Helvetica", 14),
                                bg="#A4B465", fg="white", activebackground="#FF85B3",
                                command=self.root.quit)
        quit_button.pack(pady=10)

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
                    self.create_piece(row, col, "black", is_queen=False)
        for row in range(5, 8):
            for col in range(BOARD_SIZE):
                if (row + col) % 2 != 0:
                    self.create_piece(row, col, "white", is_queen=False)

    def create_piece(self, row, col, color, is_queen):
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        outline = "gold" if is_queen else "gray"
        piece = self.canvas.create_oval(
            x - 20, y - 20, x + 20, y + 20,
            fill=color, outline=outline, width=3
        )
        self.pieces[piece] = (row, col, color, is_queen)

    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        clicked_piece = self.get_piece_at(row, col)

        if self.selected_piece:
            selected_row, selected_col, color, is_queen = self.pieces[self.selected_piece]
            if clicked_piece:
                return
            if self.is_valid_move(self.selected_piece, row, col):
                self.try_capture(selected_row, selected_col, row, col)
                self.move_piece(self.selected_piece, row, col)
                self.promote_to_queen(self.selected_piece)
                self.selected_piece = None
                self.check_for_winner()
                self.switch_turn()
        elif clicked_piece:
            r, c, color, _ = self.pieces[clicked_piece]
            if color == self.turn:
                self.selected_piece = clicked_piece

    def get_piece_at(self, row, col):
        for piece_id, (r, c, _, _) in self.pieces.items():
            if r == row and c == col:
                return piece_id
        return None

    def move_piece(self, piece_id, new_row, new_col):
        x = new_col * CELL_SIZE + CELL_SIZE // 2
        y = new_row * CELL_SIZE + CELL_SIZE // 2
        _, _, color, is_queen = self.pieces[piece_id]
        self.canvas.coords(piece_id, x - 20, y - 20, x + 20, y + 20)
        self.pieces[piece_id] = (new_row, new_col, color, is_queen)

    def promote_to_queen(self, piece_id):
        row, col, color, is_queen = self.pieces[piece_id]
        if not is_queen:
            if (color == "white" and row == 0) or (color == "black" and row == BOARD_SIZE - 1):
                self.pieces[piece_id] = (row, col, color, True)
                self.canvas.itemconfig(piece_id, outline="gold")

    def is_valid_move(self, piece_id, new_row, new_col):
        if self.get_piece_at(new_row, new_col):
            return False

        row, col, color, is_queen = self.pieces[piece_id]
        dr = new_row - row
        dc = new_col - col

        if not is_queen:
            if abs(dr) == 1 and abs(dc) == 1:
                if (color == "white" and dr == -1) or (color == "black" and dr == 1):
                    return True
            if abs(dr) == 2 and abs(dc) == 2:
                mid_row = (row + new_row) // 2
                mid_col = (col + new_col) // 2
                middle_piece = self.get_piece_at(mid_row, mid_col)
                if middle_piece:
                    _, _, middle_color, _ = self.pieces[middle_piece]
                    if middle_color != color:
                        return True
        else:
            step_r = 1 if dr > 0 else -1
            step_c = 1 if dc > 0 else -1
            if abs(dr) != abs(dc):
                return False
            r, c = row + step_r, col + step_c
            captured = None
            while r != new_row and c != new_col:
                piece = self.get_piece_at(r, c)
                if piece:
                    _, _, pc_color, _ = self.pieces[piece]
                    if pc_color == color or captured is not None:
                        return False
                    captured = piece
                r += step_r
                c += step_c
            return True

        return False

    def try_capture(self, old_row, old_col, new_row, new_col):
        dr = new_row - old_row
        dc = new_col - old_col
        if abs(dr) == 2 and abs(dc) == 2:
            mid_row = (old_row + new_row) // 2
            mid_col = (old_col + new_col) // 2
            captured = self.get_piece_at(mid_row, mid_col)
            if captured:
                self.canvas.delete(captured)
                del self.pieces[captured]
        else:
            step_r = 1 if dr > 0 else -1
            step_c = 1 if dc > 0 else -1
            r, c = old_row + step_r, old_col + step_c
            while r != new_row and c != new_col:
                piece = self.get_piece_at(r, c)
                if piece:
                    self.canvas.delete(piece)
                    del self.pieces[piece]
                    break
                r += step_r
                c += step_c

    def switch_turn(self):
        self.turn = "black" if self.turn == "white" else "white"
        self.turn_label.config(text=f"Хід {'білих' if self.turn == 'white' else 'чорних'}")

    def check_for_winner(self):
        white_pieces = [p for p in self.pieces.values() if p[2] == "white"]
        black_pieces = [p for p in self.pieces.values() if p[2] == "black"]

        if not white_pieces:
            self.show_winner("чорні")
        elif not black_pieces:
            self.show_winner("білі")

    def show_winner(self, winner_color):
        self.board_frame.destroy()
        win_frame = tk.Frame(self.root, padx=50, pady=50, bg="#F5ECD5")
        win_frame.pack()

        tk.Label(win_frame, text=f"Перемогли {winner_color}!", font=("Georgia", 24), bg="#F5ECD5").pack(pady=20)

        tk.Button(win_frame, text="Вийти", font=("Helvetica", 16), width=15,
                  bg="#A4B465", fg="white", activebackground="#FF85B3",
                  command=self.root.quit).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = CheckersApp(root)
    root.mainloop()
