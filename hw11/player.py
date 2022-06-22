import card
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, ai):
        self.name = name
        self.card = card.Card()
        self.ai = ai

    @abstractmethod
    def move(self, barrel):
        pass


class UserPlayer(Player):
    def __init__(self, *args, **kwargs):
        super(UserPlayer, self).__init__(*args, **kwargs, ai=False)

    def move(self, barrel):
        answer = input('Зачеркнуть цифру? (y/n): ').lower()
        barrel_in = self.card.barrel_in(barrel)

        if (answer == 'y') and (not barrel_in) or (answer == 'n') and barrel_in:
            print('Вы проиграли!')
            exit(0)
        elif barrel_in:
            self.card.cross_barrel(barrel)


class AIPlayer(Player):
    def __init__(self, *args, **kwargs):
        super(AIPlayer, self).__init__(*args, **kwargs, ai=True)

    def move(self, barrel):
        if self.card.barrel_in(barrel):
            self.card.cross_barrel(barrel)
