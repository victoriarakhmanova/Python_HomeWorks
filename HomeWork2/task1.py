# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
## Пример:
## - 6782 -> 23
# - 0,56 -> 11


# number = input('Enter the number: ')
# result = 0
# for i in number:
#     if i.isdigit():
#         result += int(i)
#         print(i)
# print("Sum of digits =", result)

def sum_of_digits(num):
    result = 0
    for i in num:
        if i.isdigit():
            result += int(i)

    return result

a = input('Enter the number: ')
print('Sum of digits is')
print(sum_of_digits(a))