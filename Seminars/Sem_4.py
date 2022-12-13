# def calc1(x):
#     return x+10

# # print(calc1(20))

# def calc2(x):
#     return x*30

# # print(calc2(5))

# def math(op, x):
#     print(op(x))

# math(calc1, 10)
# math(calc2, 3)

# *******

# def sum(x, y):
#     return x+y

# sum = lambda x, y: x + y # то же самое что функция выше

# def mult(x, y):
#     return x*y 

# def calc(op, a, b): 
#     print(op(a, b))

# calc(lambda x, y: x + y, 3, 7)

# *******

# list = []

# for i in range(1, 101):  
#     if(i%2 == 0):
#         list.append(i)

# print(list)

# *******

# def f(x):
#     return x**3

# list = [(i,f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list) 

# *******
# Прочитать файл, найти чётные числа и возвести в квадрат
# 1ый вариает

# f = open('get_even_num.txt', 'r')
# even_num = f.read() + ' '
# f.close()

# print(even_num)

# numbers = []

# while even_num != '':
#     space_pos = even_num.index(' ')
#     numbers.append(int(even_num[:space_pos]))
#     even_num = even_num[space_pos + 1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

# ******
# 2ой вариант

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# ******

# li = [x for x in range(1, 20)]

# li = list(map(lambda x:x+10, li)) #каждый элемент увеличили на 10
# print(li)

# ******

# data = list(map(int,input().split()))
# print(data)

# ******

# 3ий вариант

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 15 23 38'.split()

# res = map(int, data) # select заменили на map
# res = where(lambda x: not x % 2, res) 
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# ******

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)

# ******

# data = '1 2 3 5 15 23 38'.split()

# res = map(int, data) # select заменили на map
# res = filter(lambda x: not x % 2, res) 
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# ******

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 333, 555]

# data = list(zip(users, ids, salary)) объединяет все списки
# print(data)

# ******

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 333, 555]

# data = list(enumerate(users))
# print(data)
