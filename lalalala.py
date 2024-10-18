


def main():

    config = config()
    min_number = config.get('game_min_number', cast=int)
    max_number = config.get('game_max_number', cast=int)
    max_attempts = config.get('game_max_attempts', cast=int)
    starting_capital = config.get('game_starting_capital', cast=int)


    start_game(min_number, max_number, max_attempts, starting_capital)

if __name__ == '__main__':    main()

import random


def start_game(min_number, max_number, max_attempts, starting_capital):
    capital = starting_capital
    attempts_left = max_attempts
    target_number = random.randint(min_number, max_number)

    print(f"Добро пожаловать в игру! Ваш начальный капитал: {capital}")
    print(f"Задача: угадать число от {min_number} до {max_number}")
    print(f"У вас есть {attempts_left} попыток.")

    while attempts_left > 0 and capital > 0:
        print(f"\nВаш капитал: {capital}. Осталось попыток: {attempts_left}")
        try:
            bet = int(input("Сделайте ставку (введите число): "))
            if bet > capital:
                print("У вас недостаточно капитала для такой ставки.")
                continue
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        guess = int(input(f"Введите ваше предположенное число от {min_number} до {max_number}: "))

        if guess == target_number:
            print("Поздравляем! Вы угадали число!")
            capital += bet  # Удваиваем ставку
        else:
            print(f"Вы не угадали. Загаданное число было: {target_number}")
            capital -= bet  # Потеряйте ставку

        attempts_left -= 1

        if capital <= 0:
            print("У вас закончился капитал! Игра окончена.")
            break
    else:
        if attempts_left == 0:
            print("У вас закончились попытки! Игра окончена.")
            print(f"Ваш итоговый капитал: {capital}")


