from random import randint, choice

class MontyHall(object):

    def __init__(self):
        self.doors = [1, 2, 3]
        self.winner = randint(1,3)
        self.losers = [x for x in range(1,4) if x != self.winner]

    def make_first_guess(self):
        self.guess = randint(1,3)

    def open_first_door(self):
        if self.guess == self.winner:
            self.open_door = self.losers.pop(self.losers.index(choice(self.losers)))
        elif self.guess != self.winner:
            for i, door in enumerate(self.losers):
                if door == self.guess:
                    pass
                elif door != self.guess:
                    self.open_door = self.losers.pop(i)

    def switch_door(self):
        for door in self.doors:
            if door == self.open_door:
                pass
            elif door == self.guess:
                pass
            else:
                self.guess2 = door
        self.guess = self.guess2

    def evaluate_win(self):
        if self.guess == self.winner:
            return 'win'
        else:
            return 'lose'

if __name__ == "__main__":
    game = MontyHall()
    game.make_first_guess()
    print('first guess: {}'.format(game.guess))
    game.open_first_door()
    print('Monty opens door: {}'.format(game.open_door))
    yn = input('do you want to switch doors?')
    if yn == 'y':
        game.switch_door()
        print('you switch to door: {}'.format(game.guess))
    if yn == 'n':
        print('you stick with door: {}'.format(game.guess))
    print('you {}!'.format(game.evaluate_win()))

