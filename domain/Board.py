from random import randint


class Board:
    def __init__(self, dim, max_apples):
        """
        board[i][j] = 0 - empty space
        board[i][j] = 1 - apple
        board[i][j] = 2 - snake body
        board[i][j] = 3 - snake head
        :param dim:
        """
        self.board = [[0 for i in range(dim+2)]for j in range(dim+2)]
        self.dim = dim
        self.apples = 0
        self.max_apples = max_apples

    def add_apple(self):
        for t in range(100000):
            i = randint(1, self.dim)
            j = randint(1, self.dim)
            if self.available(i, j):
                self.board[i][j] = 1
                self.apples += 1
                return True
        return False

    def available(self, i, j):
        if self.board[i][j] != 0:
            return False
        if self.board[i - 1][j] == 1 or self.board[i + 1][j] == 1 or self.board[i][j - 1] == 1 or \
                self.board[i][j + 1] == 1:
            return False
        return True

    def add_apples(self):
        while self.apples < self.max_apples:
            if not self.add_apple():
                return

    def __str__(self):
        txt = ''
        for i in range(1, self.dim + 1):
            for j in range(1, self.dim + 1):
                txt += '--'
            txt += '\n'
            txt += '|'
            for j in range(1, self.dim + 1):
                if self.board[i][j] == 0:
                    txt += ' '
                elif self.board[i][j] == 1:
                    txt += '.'
                elif self.board[i][j] == 2:
                    txt += '+'
                elif self.board[i][j] == 3:
                    txt += '*'
                txt += '|'
            txt += '\n'
        return txt
