# words.txt from http://www-01.sil.org/linguistics/wordlists/english/

import random


class RandomWords:
    def __init__(self):
        self.word_list = [word for line in open('words.txt', 'r') for word in line.split()]

    def get_random_word(self):
        return random.choice(self.word_list)

    def get_random_phrase(self, num_words=4):
        return ''.join(random.choice(self.word_list) + ' ' for i in range(num_words))
