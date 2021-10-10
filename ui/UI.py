from service.Game import Game


class UI:
    def __init__(self):
        self.game = Game('settings.txt')

    @staticmethod
    def get_command():
        cmd = input(">>")
        tokens = cmd.strip().split(' ', 1)
        command_word = tokens[0].lower().strip()
        command_params = tokens[1].strip() if len(tokens) == 2 else ''

        return command_word, command_params

    def print_board(self):
        print(str(self.game.snake.board))

    def start(self):
        self.game.initialise_board()
        done = False
        while not done:
            self.game.snake.board.add_apples()
            self.print_board()
            try:
                cmd_name, cmd_params = self.get_command()
                if cmd_name == 'move':
                    self.game.move(cmd_params)
                elif cmd_name in ['up', 'down', 'left', 'right']:
                    self.game.change_direction(cmd_name)

                elif cmd_name == 'exit':
                    done = True
                else:
                    print("Invalid command")
            except Exception as error:
                print(str(error))
                done = True


ui = UI()
ui.start()
