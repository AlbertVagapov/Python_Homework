# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 1

# num = int(input("Введите число: ")) ## 10
# i = 2 # первый простой множитель
# lst = []
# old = num  ## 10
# while i <= num:  ## 2 <= 10; 2 <=5; 3 <= 5; 5 = 5; 2 <= 1(false)
#     if num % i == 0:  # Если остаток от деления на 2 равно 0  ## true; false; true
#         lst.append(i) # Добавляем в список lst  ## [2, 5]
#         num //= i # Или num = num // i Целочисленное деление ## 5; 1
#         i = 2
#     else:
#         i += 1 # 3
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Задача №2: Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst] # метод if . not in . исключает всякие повторения
# print(f"Список из неповторяющихся элементов: {new_lst}")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».

# from functions import get_list_data
# from typing import List


# def elements_to_caps(lst: list, trigger_str: str) -> List[str]:

#     for i in range(len(lst)):
#         if trigger_str in lst[i]:
#             lst[i] = lst[i].upper()
#     return lst

# lst = get_list_data(r'C:\Users\mI\OneDrive\Документы\GeekBrains\2_Seminars\Python\Homework\Sem_1\Students.txt')

# print(elements_to_caps(lst, '5'))

# with open(r'C:\Users\mI\OneDrive\Документы\GeekBrains\2_Seminars\Python\Homework\Sem_1\Students.txt', 'w', encoding = 'utf-8') as data:
#     for i in range(len(lst)):
#         data.writelines(f'{lst[i]}\n')

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, 
# считывает текст и дешифровывает его.

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



# text = '''
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо — песнь заводит,
# Налево — сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух… там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# '''

# import string

# eng_abc = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
# rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.punctuation

# def crypt_text(text:str, key:int, decrypted = False):
#     new_text = ''
#     key = key if not decrypted else - key 
#     for index, letter in enumerate(text.lower()):
#         use_abc = rus_abc if letter in rus_abc else eng_abc
#         letter_index = use_abc.find(letter)
#         new_place = (letter_index + key) % len(rus_abc)
#         if letter in rus_abc:
#             new_text += use_abc[new_place]
#         else:
#             new_text += letter 
#     return new_text

# crypted_text = crypt_text(text, 3)
# print(crypted_text)
# encrypted_text = crypt_text(crypted_text, 3, decrypted = True)
# print(encrypted_text)






