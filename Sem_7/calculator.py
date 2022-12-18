# from tkinter import *


# class Main(Frame):
#     def __init__(self, root):
#         super(Main, self).__init__(root)
#         self.build()

#     def build(self):
#         self.formula = "0"
#         self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
#         self.lbl.place(x=11, y=50)

#         btns = [
#             "C", "DEL", "*", "=",
#             "1", "2", "3", "/",
#             "4", "5", "6", "+",
#             "7", "8", "9", "-",
#             "(", "0", ")", "X^2"
#         ]

#         x = 10
#         y = 140
#         for bt in btns:
#             com = lambda x=bt: self.logicalc(x)
#             Button(text=bt, bg="#FFF",
#                    font=("Times New Roman", 15),
#                    command=com).place(x=x, y=y,
#                                       width=115,
#                                       height=79)
#             x += 117
#             if x > 400:
#                 x = 10
#                 y += 81

#     def logicalc(self, operation):
#         if operation == "C":
#             self.formula = ""
#         elif operation == "DEL":
#             self.formula = self.formula[0:-1]
#         elif operation == "X^2":
#             self.formula = str((eval(self.formula))**2)
#         elif operation == "=":
#             self.formula = str(eval(self.formula))
#         else:
#             if self.formula == "0":
#                 self.formula = ""
#             self.formula += operation
#         self.update()

#     def update(self):
#         if self.formula == "":
#             self.formula = "0"
#         self.lbl.configure(text=self.formula)


# if __name__ == '__main__':
#     root = Tk()
#     root["bg"] = "#000"
#     root.geometry("485x550+200+200")
#     root.title("Калькулятор")
#     root.resizable(False, False)
#     app = Main(root)
#     app.pack()
#     root.mainloop()


# ******
# 2

num1 = input("First Number:\n")
operator = input("Operator (+, -, *, /):\n")
num2 = input("Second Number:\n")

num1 = float(num1)
num2 = float(num2)

out = None

if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2
    
print("Answer: " + str(out))

# ******
# 3


# from operator import pow, truediv, mul, add, sub  

# operators = {
#   '+': add,
#   '-': sub,
#   '*': mul,
#   '/': truediv
# }

# def calculate(s):
#     if s.isdigit():
#         return float(s)
#     for c in operators.keys():
#         left, operator, right = s.partition(c)
#         if operator in operators:
#             return operators[operator](calculate(left), calculate(right))

# calc = input("Type calculation:\n")
# print("Answer: " + str(calculate(calc)))