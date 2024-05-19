import random
import time

start = time.time()
stop = time.time()

choices_dict = {
    'камень': 1,
    'ножницы': 2,
    'бумага': 3
}

loses_to = {
    1: 3,
    2: 1,
    3: 2
}

player_counter = 0
computer_counter = 0

def get_player_choice():
    while True:
        player_action = input('Введите вариант хода: ').lower()  # запрашиваем вариант хода у игрока
        if player_action in choices_dict:  # проверяем, что вариант хода существует в словаре choices_dict
            return choices_dict[player_action]  # возвращаем числовое значение выбора игрока

def determine_winner(player_action, computer_action):
    if loses_to[player_action] == computer_action:  # если выбор игрока проигрывает компьютеру
        return 'computer'  # возвращаем 'computer' как победителя
    elif loses_to[computer_action] == player_action:  # если выбор компьютера проигрывает игроку
        return 'player'  # возвращаем 'player' как победителя
    else:
        return 'tie'  # возвращаем 'tie' в случае ничьей

def play_game():
    global player_counter
    global computer_counter

    computer_action = random.choice(list(choices_dict.values()))  # компьютер выбирает случайный ход из словаря
    player_action = get_player_choice()  # игрок делает свой выбор

    print(f'Компьютер выбрал {list(choices_dict.keys())[list(choices_dict.values()).index(computer_action)]}.')  # выводим выбор компьютера

    winner = determine_winner(player_action, computer_action)  # определяем победителя

    if winner == 'computer':  # если победил компьютер
        print('Побеждает компьютер.')
        computer_counter += 1  # увеличиваем счетчик побед компьютера
    elif winner == 'player':  # если победил игрок
        print('Побеждает игрок.')
        player_counter += 1  # увеличиваем счетчик побед игрока
    else:
        print('Ничья.')  # если ничья

def main():
    global player_counter
    global computer_counter

    while True:
        play_game()  # запускаем игру

        if player_counter == 3:  # если игрок выиграл 3 раза
            print('  Победил игрок!')  # выводим сообщение о победе игрока
            print(f' Time eleminated: {stop - start}')
            break  # завершаем игру

        elif computer_counter == 3:  # если компьютер выиграл 3 раза
            print('  Победил компьютер!')  # выводим сообщение о победе компьютера
            print(f' Time eleminated: {stop - start}')
            break  # завершаем игру

if __name__ == '__main__':
    main()  # запускаем игру, если файл запущен как скрипт
