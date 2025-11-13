import string
#1
tem = int(input())
if tem >= 20:
    print("Кондиционер вкл")
else: print("Кондиционер выкл")

#2
nm = int(input())
if (nm <= 2 or nm == 12):
    print("зима")
elif (nm >=3 and nm <= 5):
    print("весна")
elif (nm >= 6 and nm <= 8):
    print("лето")
else: print("осень")

#3
try:
    age = int(input("age: "))
    if age < 1:
        print("error")
    if age > 22:
        print("error")
    if age <= 2:
        hage = age * 10.5
    else:
        hage = 21 + (age - 2) * 4
    print(f'{age} собачьих годов равны {hage} человеческим')
except ValueError:
    print("error")

#4
a = input()
la = int(a[-1])
asum = sum(int(i) for i in a)
if la%2 == 0 and asum % 3 == 0:
    print("число делится на 6")
else: print("число не делится на 6")

#5
p = input()
error = []
if len(p) < 8:
    error.append("Пароль должен быть не короче 8 символов.")
if not any(ch.isupper() for ch in p):
    error.append("Пароль должен содержать хотя бы одну заглавную букву")
if not any(ch.islower() for ch in p):
    error.append("Пароль должен содержать хотя бы одну строчную букву")
if not any(ch.isdigit() for ch in p):
    error.append("Пароль должен содержать хотя бы одну цифру")
spec = set(string.punctuation)
if not any(ch in spec for ch in p):
    error.append("Пароль должен содержать хотя бы один специальный символ.")
if error:
    print("Пароль ненадёжный. Причины: ")
    for i in error:
        print("-", i)
else:
    print("Пароль надёжный")