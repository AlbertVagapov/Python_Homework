# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Задача № 3 1-го семинара 

# import random

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(0,100))
# print(numbers)
# count = 0
# maximum = numbers[0]
# for i in numbers:
#     if i > maximum:
#         maximum = i
# for i in numbers:
#     if i < maximum + maximum * 0.1 and i > maximum - maximum * 0.1: # условие определяет кол-во числел +- 10 % от максимального 
#         count +=1
# print(maximum)        
# print('Количество элементов массива, которые отличны от наибольшего элемента не более чем на 10% = ',count)  

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 1

# week_day = input("Введите день недели от 1 до 7\n")
# if week_day == 1:
#     print("monday")
# elif week_day == 2:
#     print("tuesday")
# elif week_day == 3:
#     print("wednesday")
# elif week_day == 4:
#     print("thursday")
# elif week_day == 5:
#     print("friday")
# elif week_day == 6:
#     print("saturday")
# elif week_day == 7:
#     print("sunday")
# else:
#     print("Введите число от 1 до 7")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 3

# x = float(input("Введите значение X\n"))
# y = float(input("Введите значение Y\n"))

# if x > 0 and y > 0:
#     print("Плоскость № 1")
# elif x < 0 and y > 0:
#     print("Плоскость № 2")
# elif x < 0 and y < 0:
#     print("Плоскость № 3")
# elif x > 0 and y < 0:
#     print("Плоскость № 4")
# else:
#     print("Необходимо что бы X ≠ 0 и Y ≠ 0")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 4

# quarter = float(input("Введите номер четверти\n"))
# if quarter == 1:
#     print("x∈(0, ∞) u y∈(0,∞)")
# elif quarter == 2:
#     print("x∈(-∞,0) u y∈(0,∞)")    
# elif quarter == 3:
#     print("x∈(-∞,0) u y∈(-∞,0)")
# elif quarter == 4:
#     print("x∈(0,∞) u y∈(-∞,0)")
# else:
#     print("Необходимо ввести целые числа от 1 до 4")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
