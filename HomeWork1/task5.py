# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

x1 = float(input("Enter the point coordinates X1: "))
y1 = float(input("Enter the point coordinates Y1: "))
x2 = float(input("Enter the point coordinates X2: "))
y2 = float(input("Enter the point coordinates Y2: "))
distance = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)
print(distance)
