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
