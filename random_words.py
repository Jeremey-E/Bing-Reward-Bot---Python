__author__ = 'Jeremey Ebenezer'

import random


class RandomWords:
    def __init__(self):
        self.word_list = [word for line in open('words.txt', 'r') for word in line.split()]

    def get_random_word(self):
        return random.choice(self.word_list)
