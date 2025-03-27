import random
import time

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -=self.attack_power
        print(f'{self.name} атакует {other.name} и наносит {self.attack_power} урона!')

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        player_name = input('Введите имя вашего героя: ')
        self.player = Hero(player_name)
        self.computer = Hero('Компьютерный герой')

        # добавление случайности для разнообразия
        self.player.attack_power = random.randint(15, 25)
        self.computer.attack_power = random.randint(15, 25)

        print('\nНачало игры!')
        print(f'Ваш герой: {self.player.name}, сила атаки: {self.player.attack_power}')
        print(f'Противник: {self.computer.name}, сила атаки: {self.computer.attack_power}')
        print('Битва начинается!\n')

    def start(self):
        current_round = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f'\n=== Раунд {current_round} ===')

            #ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                break

            # ход компьютера
            self.computer_turn()
            if not self.player.is_alive():
                break

            current_round += 1
            time.sleep(1) # пауза для удобства чтения

        self.declare_winner()

    def player_turn(self):
        input('\nНажмите Enter,  чтобы атаковать...')
        self.player.attack(self.computer)
        print(f'У {self.computer.name} осталось {max(0, self.computer.health)} здоровья\n')

    def computer_turn(self):
        print('\nХод противника...')
        time.sleep(1) # имитация "раздумий" компьютера
        self.computer.attack(self.player)
        print(f'У {self.player.name} осталось {max(0, self.player.health)} здоровья\n')

    def declare_winner(self):
        print('\n=== Битва окончена! ===')
        if self.player.is_alive():
            print(f'{self.player.name} побеждает с {self.player.health} очками здоровья!')
        else:
            print(f'{self.computer.name} побеждает с {self.computer.health} очками здоровья!')
        print('Спасибо за игру!')

#запуск игры
if __name__ == '__main__':
    game = Game()
    game.start()