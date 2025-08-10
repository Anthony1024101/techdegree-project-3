import random

from .phrase import Phrase

class Game():

    phrases = [
        Phrase('Just because your right does not mean your correct'),
        Phrase('Just because you want an answer does not mean you will like it'),
        Phrase('The chicken is in the freezer'),
        Phrase('Did you touch my drum set'),
        Phrase('We use to rule the world'),
        Phrase('We do not make mistakes just happy little accidents'),
        Phrase('There is no place like home'),
        Phrase('Believe you can and your halfway there'),
        Phrase('Change your thoughts and you change your world'),
        Phrase('Impossible is nothing'),
        
    ]

    def __init__(self):
        self.phrases = Game.phrases
        self.missed = 0
        self.active_phrase = None
        self.guesses = []

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        return 'Phrase Hunter game!\n' + \
            'Win by guessing all the correct letters!\n' + \
            'five more chances (5) !\n' + \
            'Exit with ctrl+C or ctrl+D\n'

    def play_game(self):
        while True:
            if self.lost() or self.win():
                break
            print(self.active_phrase.display(), '\n')
            self.handle_guess()
            print(f'{5 - self.missed} misses remaining!')

    def start(self):
        self.active_phrase = self.get_random_phrase()
        print(self.welcome())
        self.play_game()
        print('\n', self.game_over(self.win()), '\n')
        print('It is:', self.active_phrase.phrase.upper())
        


    def lost(self):
        return self.missed == 5

    def win(self):
        return self.active_phrase.check_complete()



    def handle_guess(self):
        try:
            result = self.active_phrase.check_guesses(self.get_guess())
            if result is False:
                self.missed += 1
        except ValueError as err:
            print(err)


    def game_over(self, win):
        return {
            False: 'TGame Over...',
            True: 'You Did It!'
        }[win]


    def get_guess(self):
        guess = input('Guess a letter:  ').lower()
        if len(guess) > 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
            raise ValueError('Please pick one letter.')
        elif guess in self.guesses:
            raise ValueError(f'You already guessed `{guess}`')
        else:
            self.guesses.append(guess)
        return guess


  

