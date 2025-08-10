class Phrase():

    def __init__(self, phrase):
        self.phrase = self.validate_phrase(phrase)
        self.letter_location = self.set_letter(self.phrase)
        self.blanks_phrase = self.set_blanks(self.phrase, init=True)

    def display(self):
        return self.blanks_phrase

    def check_guesses(self, guesses):
        try:
            self.change_blanks(guesses)
            return True
        except KeyError:
            return False

    def change_blanks(self, letter):
        indices = self.letter_location[letter]
        letters = self.parse_letters(self.blanks_phrase)
        for index in indices:
            letters[index] = letter
        letters = ''.join(letters)
        self.blanks_phrase = self.set_blanks(letters)

    def check_complete(self):
        return '_' not in self.blanks_phrase

    def set_blanks(self, phrase, init=False):
        blanks = []
        for word in phrase.split(' '):
            if init is True:
                letters = ['_' for letter in word]
            else:
                letters = [letter for letter in word]
            blanks.append(' '.join(letters))
        return '   '.join(blanks)

    def parse_letters(self, blanks_phrase):
        words = []
        for word in blanks_phrase.split('   '):
            word = ''.join(word.split(' '))
            words.append(word)
        return [letter for letter in ' '.join(words)]

    def set_letter(self, phrase):
        map = {}
        for index, letter in enumerate(phrase):
            try:
                map[letter].append(index)
            except KeyError:
                map[letter] = list()
                map[letter].append(index)
        return map

    def reset(self):
        self.blanks_phrase = self.set_blanks(self.phrase, init=True)

    def validate_phrase(self, phrase):
        if ' ' not in phrase or phrase == ' ':
            raise ValueError('Phrase must be more than one word')
        letters = phrase.lower()
        for letter in letters:
            if letter not in 'abcdefghijklmnopqrstuvwxyz ':
                raise ValueError(f'{letter} is not a letter or space')
        return letters