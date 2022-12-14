# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension
# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

# 5 - Есть список случайных чисел в промежутке от 1 до 200, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]


# ******
# 1


# from typing import List


# def str_enc(lst: List[str], enc: int):
#     what_find = input("Что необходимо найти?:\n>> ")
#     lst = [i[0] for i in enumerate(lst) if type(i[1]) == str and i[1] in what_find]
#     return f"Позиция {enc} вхождения {what_find} в строку:\n{lst[enc-1]}" \
#            if len(lst) >= enc else -1


# input_lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# res = str_enc(input_lst, 2)
# print(res)

# input_lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# res = str_enc(input_lst, 2)
# print(res)

# input_lst = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# res = str_enc(input_lst, 2)
# print(res)

# input_lst = ["123", "234", 123, "567"]
# res = str_enc(input_lst, 2)
# print(res)

# input_lst = []
# res = str_enc(input_lst, 2)
# print(res)

# ******
# 2

# from functions import give_int
# from functions import random_list
# from typing import List


# def pair_mult(data_list: List[int]) -> List[int]:

#     return [data_list[i]*data_list[-1 - i] for i in range(len(data_list)//2 + len(data_list) % 2)]


# dt_lst = random_list(4)
# print(dt_lst)
# res = pair_mult(dt_lst)
# print(res)

# dt_lst = random_list(5)
# print(dt_lst)
# res = pair_mult(dt_lst)
# print(res)

# ******
# 3

# from functions import give_int

# result = [(-3)**i for i in range(give_int('Type amount of numbers: '))]
# print(result)

# ******
# 5

# from functions import random_list

# lst_start = random_list(200)
# lst_tuple = [i for i in enumerate(lst_start) if i[0] != i[1]]  
# print(lst_tuple)

# # ******
# # 6

# lst_div = [i for i in lst_tuple if not (i[0]+i[1]) % 5]  # Task6
# print(lst_div)