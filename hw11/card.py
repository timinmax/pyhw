import random


class Card:
    def __init__(self):
        self.card = Card.gen_card()

    @staticmethod
    def gen_card():
        values = random.sample(range(1, 90), 15)
        card = []
        card.extend([0]*27)
        for offset in [0, 9, 18]:
            for pos in random.sample(range(offset, offset + 9), 5):
                card[pos] = values.pop()
        return card

    def __str__(self):
        card_str = '_\t' * 9 + '\n'
        for pos, val in enumerate(self.card):
            card_str += str(val) + ('\n' if pos in [8, 17] else '\t')
        card_str += '\n' + '_\t' * 9 + '\n'

        return card_str

    def barrel_in(self, barrel):
        return barrel in self.card

    def cross_barrel(self, barrel):
        self.card[self.card.index(barrel)] = '-'

    def get_summ(self):
        return sum([cell for cell in self.card if cell != '-'])
