# Вычисление с рациональными числами

def math(op, x, y):  
    print(op(x, y))

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

a = input("Ведите первую цифру:\n")
operator = input("Оператор (+, -, *, /):\n")
b = input("Ведите вторую цифру:\n")

a = float(a)
b = float(b)

out = None

if operator == "+":
    math(sum, a, b)
elif operator == "-":
    math(sub, a, b)
elif operator == "*":
    math(mult, a, b)
elif operator == "/":
    math(div, a, b)

