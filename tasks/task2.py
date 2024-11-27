# 1. Сумма квадратов чисел
# Найди сумму квадратов чисел от 1 до 10 включительно.
# # Ожидаемый результат:
# 385

""" print(sum(x**2 for x in range(1,11))) """

# 2. Переверни строку
# Напиши программу, которая переворачивает строку задом наперед.
# Пример ввода:
# Привет
# Пример вывода:
# тевирП

""" print("Привет"[::-1]) """

# 3. Четные числа
# С помощью list comprehension создай список всех четных чисел от 1 до 20.
# Пример:
# # Ожидаемый результат:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

""" print([x for x in range(1,21) if x % 2 == 0]) """


# 4. Подсчет гласных
# Напиши функцию, которая считает количество гласных букв в строке.
# Пример ввода:
# Программирование
# Пример вывода:
# 6

# если гласные идут как массив от 0 тогда sum() - 1 в противном случае ответ 7

""" print(sum(1 for x in "Программирование" if x in "аеиоуюя" )) """


# 5. Сортировка списка
# Дан список чисел. Напиши программу, которая отсортирует его по возрастанию без использования встроенных функций сортировки.
# Пример ввода:
# [5, 3, 8, 6, 2]
# Пример вывода:
# [2, 3, 5, 6, 8]

""" numbers = [5, 3, 8, 6, 2]
min_num = float("-inf")
sorted_numbers = []
while numbers:
    min_num = min(numbers)
    sorted_numbers.append(min_num)
    numbers.remove(min_num)

print(sorted_numbers) """
# ==========================================================

# 1. Числа Армстронга
# Число Армстронга — это число, которое равно сумме своих цифр, возведённых в степень, равную количеству цифр в числе.
# Напиши программу, которая проверяет, является ли заданное число числом Армстронга.
# Пример ввода:
# 153
# Пример вывода:
# True  # 153 = 1^3 + 5^3 + 3^3

""" number = 153
print(sum(int(x)**len(str(number)) for x in str(number))) """


# 2. Уникальные элементы списка
# Напиши функцию, которая принимает список чисел и возвращает список, содержащий только те числа, которые встречаются в нём ровно один раз.
# Пример ввода:
# [4, 5, 7, 5, 9, 4, 8]
# Пример вывода:
# [7, 9, 8]


""" def uniqueList(numList):
    newList = []
    for x in numList:
        if numList.count(x) == 1:
            newList.append(x)
    return newList


a = [4, 5, 7, 5, 9, 4, 8]
print(uniqueList(a)) """


# 3. Треугольник Паскаля
# Напиши функцию, которая генерирует первые n строк треугольника Паскаля.
# Пример ввода:
# n = 5
# Пример вывода:
# [
#  [1],
#  [1, 1],
#  [1, 2, 1],
#  [1, 3, 3, 1],
#  [1, 4, 6, 4, 1]
# ]


#            0C0
#         1C0   1C1
#      2C0   2C1   2C2
#   3C0   3C1   3C2   3C3

# Не супер эффективный способ но рабочий по формуле :D

""" def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def combinatoric(n, m):
    if n == 0 and m == 0:
        return 1
    return factorial(n) // (factorial(m) * factorial(n - m))


def pascalTriangle(n):
    pascal = []
    for x in range(n):
        row = []
        for y in range(x+1):
            row.append(combinatoric(x,y))
        pascal.append(row)
    print(pascal)

pascalTriangle(5) """


# 4. Проверка анаграмм
# Напиши функцию, которая проверяет, являются ли две строки анаграммами (состоят из одинаковых букв).
# Пример ввода:
# "listen", "silent"
# Пример вывода:
# True
# Я так понял что дается массив нужно проверить все слова


""" def isAnagram(listItem) -> bool:
    if len(set(["".join(sorted(x)) for x in listItem])) == 1:
        return True
    else:
        return False
"""


# 5. Числа Фибоначчи с мемуизацией
# Напиши функцию, которая возвращает n-е число Фибоначчи, используя мемуизацию для оптимизации.
# Пример ввода:
# n = 10
# Пример вывода:
# 55

""" def fibo_mem(func):
    memo = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in memo:
            memo[key] = func(*args, **kwargs)
        return memo[key]
    return wrapper

@fibo_mem
def Fibonacci(pos) -> int:
    return int((((1 + (5**0.5)) / 2) ** pos + ((1 - (5**0.5)) / 2) ** pos) // (5**0.5))

print(Fibonacci(10)) """


# 6. Таблица умножения в виде матрицы
# Напиши программу, которая создаёт двумерный список (матрицу) 
# размером n x n, где элемент в ячейке [i][j] равен произведению i * j.
# Пример ввода:
# n = 3
# Пример вывода:
# [
#  [1, 2, 3],
#  [2, 4, 6],
#  [3, 6, 9]
# ]

matrix = [[] for x in range(1,4)]
print(matrix)