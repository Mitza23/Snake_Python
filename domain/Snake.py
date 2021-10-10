class Cell:
    def __init__(self, i, j):
        self.lin = int(i)
        self.col = int(j)


class Snake:
    def __init__(self, board):
        self.board = board
        self.len = 3
        column = self.board.dim/2 + 1
        line = (self.board.dim - 3)/2 + 1
        self.positions = [Cell(line, column), Cell(line+1, column), Cell(line+2, column)]
        self.dir = 1  # 1-N  2-E  3-S  4-W

    def place_snake(self):
        for i in range(1, self.len):
            # print(self.positions[i].lin, self.positions[i].col)
            self.board.board[self.positions[i].lin][self.positions[i].col] = 2

        if self.board.board[self.positions[0].lin][self.positions[0].col] not in [0, 1]:
            raise ValueError("GAME OVER")
        if self.positions[0].lin < 1 or self.positions[0].lin > self.board.dim:
            raise ValueError("GAME OVER")
        if self.positions[0].col < 1 or self.positions[0].col > self.board.dim:
            raise ValueError("GAME OVER")

        self.board.board[self.positions[0].lin][self.positions[0].col] = 3

    def move_snake_1(self):
        end_lin = self.positions[-1].lin
        end_col = self.positions[-1].col

        for i in range(self.len - 1, 0, -1):
            self.positions[i].lin = self.positions[i-1].lin
            self.positions[i].col = self.positions[i-1].col

        if self.dir == 1:
            self.positions[0].lin -= 1
        elif self.dir == 2:
            self.positions[0].col += 1
        elif self.dir == 3:
            self.positions[0].lin += 1
        elif self.dir == 4:
            self.positions[0].col -= 1

        if self.board.board[self.positions[0].lin][self.positions[0].col] == 0:
            self.board.board[end_lin][end_col] = 0
        elif self.board.board[self.positions[0].lin][self.positions[0].col] == 1:
            self.len += 1
            self.board.apples -= 1
            self.positions.append(Cell(end_lin, end_col))

        # for cell in self.positions:
        #     print(cell.lin, cell.col)
        # print(self.board)
        self.clear_snake()

        self.place_snake()

    def clear_snake(self):
        for cell in self.positions:
            self.board.board[cell.lin][cell.col] = 0


