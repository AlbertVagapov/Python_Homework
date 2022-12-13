# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# 3- Создайте программу для игры в ""Крестики-нолики"". Для определения победы вам может пригодиться функция filter. Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода

# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

# Дополнительно(по желанию):
# 5 - Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.

# P.S. Не знаете, как подступиться к 5-й задаче? Небольшая помощь: https://disk.yandex.ru/d/Unjq7ClMg-6EOw

# ******

# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

# input_str = (input('Введите текст\n')).lower()
# trigger_str = input('Введите искомую строку с маленькой буквы\n')
# lst = [i for i in input_str.split(' ') if not trigger_str in i]
# print(' '.join(lst))

# ******

# 2

# from functions import give_int
# from typing import List
# from random import randint


# def player_logic(player_name: str, turn_limitation: int = 28, num: int = 74) -> int:

#     sweet = 0
#     while not 0 < sweet <= turn_limitation:
#         sweet = give_int(
#             f'{player_name}, сколько конфет вы хотите взять?\n', 1)
#         if sweet > turn_limitation:
#             print(f'Вы не можете взять больше, чем{turn_limitation}')
#         elif sweet > num:
#             print(f'Вы не можете взять больше, чем{num}')

#     return sweet


# def bot_logic(player_name: str, turn_limitation: int = 28, num: int = 74) -> int:
#     sweet = 0
#     if player_name == 'Hard Bot':
#         if num <= turn_limitation:
#             sweet = num
#         else:
#             if num % turn_limitation > 1:
#                 sweet = turn_limitation - 1
#             else:
#                 sweet = turn_limitation - turn_limitation + 1
#     elif player_name == 'Easy Bot':
#         if num <= turn_limitation:
#             sweet = num
#         else:
#             sweet = randint(1, 28)
#     print(f'{player_name} берет {sweet} конфет')
#     return sweet


# def turn_maker(player_tuple: List[tuple], number: int = 74) -> None:
#     first_turn = randint(0, 1)
#     while number != 0:
#         if player_tuple[first_turn][2] == 'man':
#             sweet_amount = player_logic(
#                 player_name=player_tuple[first_turn][1], num=number)
#         elif player_tuple[first_turn][2] == 'bot':
#             sweet_amount = bot_logic(
#                 player_name=player_tuple[first_turn][1], num=number)
#         number -= sweet_amount
#         print(f'осталось {number} конфет\n')
#         if number <= 0:
#             exit(print(f'Победил {player_tuple[first_turn][1]}'))
#         else:
#             if first_turn:
#                 first_turn = 0
#             else:
#                 first_turn = 1


# def menu_input() -> None:
#     while True:
#         print('Нажмите 1 для игры вдвоем')
#         print('Нажмите 2 для игры против бота')
#         print('Нажмите -1 для выхода')
#         num = input('Введите цифру:\n')
#         if num == '1':
#             pl_list = [(0, input('Введите имя первого игрока:\n'), 'man'),
#                        (1, input('Введите имя второго игрока:\n'), 'man')]
#             turn_maker(pl_list)
#         elif num == '2':
#             level = 0
#             while level not in (1, 2):
#                 level = give_int('Выберите сложность бота\n'
#                                  '1 - сложный\n'
#                                  '2 - простой\n', 1)
#                 if level > 2:
#                     print('Попробуйте еще  раз')
#             if level == 1:
#                 pl_list = [(0, input('Введите имя первого игрока:\n'), 'man'),
#                            (1, 'Hard Bot', 'bot')]
#             else:
#                 pl_list = [(0, input('Введите имя первого игрока:\n'), 'man'),
#                            (1, 'Easy Bot', 'bot')]
#             turn_maker(pl_list)
#         elif num == '-1':
#             return exit(print('Вы вышли из игры'))
#         else:
#             print('Попробуйте еще раз')


# menu_input()


# ******


# from typing import List
# from functions import give_int


# def draw_board(area: List) -> List:
#     '''
#     Функция, выводящая на консоль игровое поле из 9 пронумерованных клеток
#     '''    
#     print('│', area[1], '│', area[2], '│', area[3], '│')
#     print('│', area[4], '│', area[5], '│', area[6], '│')
#     print('│', area[7], '│', area[8], '│', area[9], '│')


# def game(players: List, area: List) -> None:
#     '''
#     Логика игры
#     arg players: список игроков
#     arg area: список номеров клеток игрового поля
#     '''   
#     pl = players[0]
#     for i in range(len(area) - 1):
#         new_turn = 10
#         while new_turn > 9 or area[new_turn] in ('X', 'O'):
#             new_turn = give_int(
#                 f'{pl[1]}, куда поставить отметку? Введите число от 1 до 9:', 1)
#             if new_turn > 9 or area[new_turn] in ('X', 'O'):
#                 print('Эта клетка уже занята\n')
#         if pl == players[0]:
#             area[new_turn] = 'X'
#             draw_board(area)
#             if i >= 4:
#                 check_win(area, players[0])
#             pl = players[1]
#         else:
#             area[new_turn] = 'O'
#             draw_board(area)
#             if i >= 4:
#                 check_win(area, players[1])
#             pl = players[0]


# def check_win(area: List, players: List) -> None:
#     '''
#     Функция, проверяющая выигрышные комбинации
#     arg players: список игроков
#     arg area: список номеров клеток игрового поля
#     '''   
#     if area[1] == area[2] == area[3]\
#             or area[4] == area[5] == area[6]\
#             or area[7] == area[8] == area[9]\
#             or area[1] == area[4] == area[7]\
#             or area[2] == area[5] == area[8]\
#             or area[3] == area[6] == area[9]\
#             or area[1] == area[5] == area[9]\
#             or area[3] == area[5] == area[7]:
#         return exit(print(f'{players[1]} победил!'))
#     else:
#         return


# area = list(range(10))
# pl1 = input('Введите имя первого игрока:\n')
# pl2 = input('Введите имя второго игрока:\n')
# players = [[1, pl1], [2, pl2]]
# draw_board(area)
# game(players, area)


