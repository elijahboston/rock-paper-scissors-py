import sys
import random


MOVES = {
    'ROCK': 'ROCK',
    'PAPER': 'PAPER',
    'SCISSORS': 'SCISSORS'
}

WEAKNESS = {
    MOVES['ROCK']: MOVES['PAPER'],
    MOVES['PAPER']: MOVES['SCISSORS'],
    MOVES['SCISSORS']: MOVES['ROCK']
}


def count_moves(user_moves):
    counts = [
        {'name': MOVES['ROCK'], 'played': 0},
        {'name': MOVES['PAPER'], 'played': 0},
        {'name': MOVES['SCISSORS'], 'played': 0}
    ]

    for move in counts:
        move['played'] = user_moves.count(move['name'])

    return sorted(counts, key=lambda k: k['played'])


class Game:

    def __init__(self):
        self.user_move = ''
        self.computer_move = ''
        self.winner = ''
        self.round = 0
        self.score = [0, 0]
        self.user_move_history = []

    def start(self):
        self.new_round()

    def new_round(self):
        self.round = self.round + 1
        self.prompt_for_move()
        self.get_computer_move()
        self.who_wins()
        self.display_round_results()
        self.prompt_new_round()

    def prompt_for_move(self):
        user_move_input = input('[r]ock [p]aper [s]cissors\n').lower()
        valid_move = False

        if user_move_input.startswith('r'):
            self.user_move = MOVES['ROCK']
            valid_move = True

        if user_move_input.startswith('p'):
            self.user_move = MOVES['PAPER']
            valid_move = True

        if user_move_input.startswith('s'):
            self.user_move = MOVES['SCISSORS']
            valid_move = True

        if not valid_move:
            print('Invalid move, try again...')
            self.prompt_for_move()
        else:
            self.user_move_history.append(self.user_move)

    def get_computer_move(self):
        if len(self.user_move_history) > 2:
            most_played_move = count_moves(self.user_move_history)[-1]['name']

            # print('Most played move: {}'.format(most_played_move))

            best_possible_moves = list(MOVES.keys())
            best_possible_moves.remove(most_played_move)

            # print('Best moves: {}'.format(best_possible_moves))

            self.computer_move = best_possible_moves[random.randint(0, 1)]
        else:
            self.computer_move = list(MOVES.keys())[random.randint(0, 2)]

    def who_wins(self):
        if WEAKNESS[self.user_move] == self.computer_move:
            self.winner = 'COMPUTER'
            self.score[1] = self.score[1] + 1
        elif self.user_move == self.computer_move:
            self.winner = 'TIE'
        else:
            self.winner = 'YOU'
            self.score[0] = self.score[0] + 1

    def display_round_results(self):
        print('>>> Round {} <<<'.format(self.round))
        print('{} (User) vs {} (Computer)'.format(self.user_move, self.computer_move))
        print('Winner: {}!'.format(self.winner))
        print('~~ Score: {}/{} ~~'.format(self.score[0], self.score[1]))

    def prompt_new_round(self):
        new_round_input = input('Play again? [Y]es [N]o\n')

        if new_round_input.lower().startswith('y'):
            self.new_round()
        else:
            sys.exit()


game = Game()
game.start()
