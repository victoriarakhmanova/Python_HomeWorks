#Реализуйте алгоритм перемешивания списка.
import random
def mix_list(original):
    copy = original[:]
    copy_length = len(original)
    for i in range(copy_length):
        index = random.randint(0, copy_length - 1)
        temp = copy[i]
        copy[i] = copy[index]
        copy[index] = temp
    return copy
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)
