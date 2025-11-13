#1
a = [5, 1, 9, 3, 7, 2, 8, 4, 6, 0]
for i in a:
    if a[i] == 3:
        a[i] = 30
print(a)

#2
a1 = [5, 1, 9, 3, 7]
b1 = [i ** 2 for i in a1]
print(b1)

#3
f = [5, 1, 9, 3, 7]
print(max(f)/len(f))

#4
t = (5, 2, 9, 1, 7)
if all(isinstance(x, (int, float)) for x in t):
    t = tuple(sorted(t))
    print(t)
else:
    print("error: ", t)

#5
goods = {"яблоки": 10, "груши": 15, "бананы": 20}
min_g = min(goods, key=goods.get)
max_g = max(goods, key=goods.get)
print(f'{min_g} {goods[min_g]}, {max_g} {goods[max_g]}')

#6
x = [1, 2, 3, 4]
y = {k: k for k in x}
print(y)

#7
d = {"hello": "привет", "cat": "кот", "car": "машина"}
s = input('Введите слово: ')
if s in d.values():
    for key, value in d.items():
        if value == s:
            print(f'Перевод: {key}')

#8
import random
va = ['Камень', 'Ножницы', 'Бумага', 'Ящерица', 'Спок']
va_user = input('Введите ваш вариант: ')
va_programm = random.choice(va)
print(f'Вариант программы: {va_programm}')
if va_user == va_programm:
    print('Ничья')
elif (va_user == 'Камень' and (va_programm == 'Ножницы' or va_programm == 'Ящерица')) or \
     (va_user == 'Ножницы' and (va_programm == 'Бумага' or va_programm == 'Ящерица')) or \
     (va_user == 'Бумага' and (va_programm == 'Камень' or va_programm == 'Спок')) or \
     (va_user == 'Ящерица' and (va_programm == 'Спок' or va_programm == 'Бумага')) or \
     (va_user == 'Спок' and (va_programm == 'Камень' or va_programm == 'Ножницы')):
    print('Победил пользователь')
else:
    print('Победила программа')