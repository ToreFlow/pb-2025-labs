#1
def time(value, from_unit, to_unit):
    i = {
        's': 1,
        'm': 60,
        'h': 3600}

    b = value * i[from_unit]
    result = b / i[to_unit]
    return result
value = int(input())
from_unit = input()
to_unit = input()
print(time(value, from_unit, to_unit), to_unit)

#2
def calculate_profit(a, n):
    if a < 30000:
        return "Error"
    sum_bonus = min(a // 10000 * 0.3, 5)
    term_rate = 3 if n <= 3 else 5 if n <= 6 else 2
    total_rate = term_rate + sum_bonus
    return a * (1 + total_rate / 100) ** n - a
a = int(input())
n = int(input())
print(calculate_profit(a, n))

#3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
a, b = map(int, input().split())
if a < 0 or b < 0 or a > b:
    print("Error!")
else:
    primes = []
    for num in range(max(2, a), b + 1):
        if is_prime(num):
            primes.append(str(num))
    if primes:
        print(" ".join(primes))
    else:
        print("Error!")

#4
n, m = map(int, input("Введите размер матрицы (строки столбцы): ").split())
if n < 2 or m < 2:
    print("Ошибка: матрица должна быть как минимум 2x2")
    exit()
print(f"\nВведите первую матрицу {n}x{m} (построчно, числа через пробел):")
matrix1 = []
for i in range(n):
    row = list(map(float, input(f"Строка {i+1}: ").split()))
    if len(row) != m:
        print(f"Ошибка: в строке должно быть {m} чисел")
        exit()
    matrix1.append(row)
print(f"\nВведите вторую матрицу {n}x{m} (построчно, числа через пробел):")
matrix2 = []
for i in range(n):
    row = list(map(float, input(f"Строка {i+1}: ").split()))
    if len(row) != m:
        print(f"Ошибка: в строке должно быть {m} чисел")
        exit()
    matrix2.append(row)
result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print("\nРезультат сложения матриц:")
for row in result:
    print(" ".join(f"{num:g}" for num in row))

#5
def is_palindrome(s):
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]
text = input()
if is_palindrome(text):
    print("Да")
else:
    print("Нет")