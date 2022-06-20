from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def cloth_volume(self):
        pass


class Coat(Clothes):
    @property
    def cloth_volume(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def cloth_volume(self):
        return 2 * self.size + 0.3


my_coat = Coat(12)
print(my_coat.cloth_volume)

my_suit = Suit(12)
print(my_suit.cloth_volume)
