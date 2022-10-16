# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }
n = int(input('Enter the number: '))
a = {}
for i in range(1, n + 1):
    a[i] = round((1+1/i) **i, 2)
    total = sum(a.values())


print(a)
print(total)