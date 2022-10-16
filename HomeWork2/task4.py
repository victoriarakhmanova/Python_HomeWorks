# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("enter the number: "))
result = 1
numbers = list(range(-n, n + 1))
print(numbers)
data = open('file.txt', 'r', encoding="utf-8")

for i in data:
    result *= numbers[int(i)]
    print(result)
print(result)
data.close()

