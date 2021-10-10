from domain.Board import Board
from domain.Snake import Snake
from ui.Settings import Settings


class Game:
    def __init__(self, file_name):
        setting = Settings(file_name)
        params = setting.get_attributes()
        board = Board(int(params[0]), int(params[1]))
        self.board = board
        self.snake = Snake(board)

    def initialise_board(self):
        self.snake.place_snake()
        self.board.add_apples()

    def move(self, cmd_params):
        if len(cmd_params) == 0:
            self.snake.move_snake_1()
        else:
            if not cmd_params.isnumeric():
                print("Number of moves must be integer")
                return
            else:
                for i in range(int(cmd_params)):
                    self.snake.move_snake_1()

    def change_direction(self, cmd_name):
        if cmd_name == 'up':
            if self.snake.dir == 3:
                print("Snakes can't 180")
            elif self.snake.dir == 1:
                return
            else:
                self.snake.dir = 1
                self.snake.move_snake_1()
        elif cmd_name == 'right':
            if self.snake.dir == 4:
                print("Snakes can't 180")
            elif self.snake.dir == 2:
                return
            else:
                self.snake.dir = 2
                self.snake.move_snake_1()
        elif cmd_name == 'down':
            if self.snake.dir == 1:
                print("Snakes can't 180")
            elif self.snake.dir == 3:
                return
            else:
                self.snake.dir = 3
                self.snake.move_snake_1()
        elif cmd_name == 'left':
            if self.snake.dir == 2:
                print("Snakes can't 180")
            elif self.snake.dir == 4:
                return
            else:
                self.snake.dir = 4
                self.snake.move_snake_1()


# game = Game()
# game.start()