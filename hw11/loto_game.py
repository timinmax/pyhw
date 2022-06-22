import player
import random


class LotoGame:
    def __init__(self):
        player_name = input('Введите имя игрока')
        self.user_player = player.UserPlayer(player_name)
        self.ai_player = player.AIPlayer('AI')
        self.barrels = []
        self.barrels.extend(range(1, 91))

    def pull_barrel(self):
        random.shuffle(self.barrels)
        return self.barrels.pop()

    def show_cards(self):
        print(self.user_player.name, '\n', self.user_player.card)
        print(self.ai_player.name, '\n', self.ai_player.card)

    def check_winner(self):
        sum_player = self.user_player.card.get_summ()
        ai_summ = self.ai_player.card.get_summ()

        if sum_player == 0 and ai_summ == 0:
            print('Ничья!')
            exit(0)
        elif sum_player == 0:
            print(f'Выиграл {self.user_player.name}')
            exit(0)
        elif ai_summ == 0:
            print(f'Выиграл {self.ai_player.name}')
            exit(0)

    def play(self):
        while True:
            self.show_cards()
            barrel = self.pull_barrel()
            print(f'Новый бочонок {barrel} (осталось {len(self.barrels)})')
            self.user_player.move(barrel)
            self.ai_player.move(barrel)
            self.check_winner()


loto = LotoGame()
loto.play()
