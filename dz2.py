# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = float(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Это не число!")
#     return number
#
#
# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum
#
#
# num = InputNumbers("Введите число: ")
#
# print(f"Сумма цифр = {sumNums(num)}")

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Факториал: 5! = 120

# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Число должно быть integer ")
#     return number
#
#
# def mult(n):
#     if n == 1:
#         return 1
#     else:
#         return n * mult(n - 1)
#
#
# num = InputNumbers("Введите число: ")
#
# list = []
# for e in range(1, num + 1):
#     list.append(mult(e))
#
# print(f"Произведения чисел от 1 до {num}:  {list}")

# Задана последовательность натуральных чисел, завершающаяся числом 0.
# Требуется определить значение второго по величине элемента в этой последовательности,
# то есть элемента, который будет наибольшим,
# если из последовательности удалить наибольший элемент.

# list_val = [1, 2.75, 25.31, 30, 10, 0]
# print(*list_val)
# list_val.sort()
# print("Значение второго по величине элемента в этой последовательности:", list_val[-2])

