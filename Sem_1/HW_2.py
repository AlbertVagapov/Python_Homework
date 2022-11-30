
# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты. Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep. Определите номер этого человека и количество монет, которые оказались у него в конце игры.

# 4 - (если не получается, то альтернативная задача). Составьте алгоритм нахождения случайного числа без использования библиотеки random.
# https://habr.com/ru/company/vk/blog/574414/ - поможет вам эта статья.

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# (-0.56) -> 11

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 1

# real_number = float(input("Введите целое: "))
# if real_number < 0:
#     real_number *= -1 # Перевод отрицательных занчений в положительные 

# result = 0

# for i in str(real_number): # Перевод в строку
#     if i != '.':
#         result += int(i)

# print(result)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 2


# number_of_elems = int(input("Пожалуйста введите целое положительное число: \n"))
# if number_of_elems <= 0:
#     print ('Вы ввели отрицательное число или ноль. Попробуйте ввести целое положительное число')
# factorial = 1
# list_factorial = []

# for i in range(1, number_of_elems + 1):
#     factorial *= i
#     list_factorial.append(factorial)

# print(list_factorial)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 3

# 3 - Дан массив размера N.
# 0. После каждого отрицательного элемента массива
# 1. вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

# import random

# list_number_of_elements = int(input("Пожалуйста введите количество элементов в массиве(целым положительным числом): \n"))
# if list_number_of_elements <= 0:
#     print("Вы ввели ноль либо отрицательное число. Пожалуйста введите целочисленное положительное число")

# random_list = []
# for i in range(0, list_number_of_elements):
#     random_number = random.randint(-50, 10)
#     random_list.append(random_number)
# print(random_list)

# new_random_list = []
# for each in random_list:
#     new_random_list.append(each)
#     if each < 0:
#         new_random_list.append(0)
# print(new_random_list)

# $$$$$$$$$$$$$$$$$$$$$$

# # 4


# def the_reader(participants, numreader):


#     for _ in range(len(participants)):
#         number_of_participants = len(participants)
#         if num_reader % number_of_participants == 0:
#             index_deleted = (num_reader % number_of_participants)
#             func_print(participants, index_deleted)
#             del participants[index_deleted - 1]
#             stop_game = len(participants)
#             if stop_game == 1:
#                 print(f'\nОстался человек под номером {participants[0]}')
#                 return
#         else:
#             index_deleted = (num_reader % number_of_participants)
#             func_print(participants, index_deleted)
#             del participants[index_deleted - 1]
#             participants = participants[index_deleted - 1:] + participants[:index_deleted - 1]
#             stop_game = len(participants)
#             if stop_game == 1:
#                 print(f'\nОстался человек под номером {participants[0]}')
#                 return


# def func_print(participants, index_deleted):
#     print(
#         f'\nТекущий круг людей: {sorted(participants)}\nНачало счета с номера {participants[0]}\nВыбывает человек под '
#         f'номером {participants[index_deleted - 1]}')

# count_participants = int(input('Сколько человек участвует: '))
# participants = list(range(1, count_participants + 1))
# num_reader = int(input('Число в считалке '))

# the_reader(participants, num_reader)