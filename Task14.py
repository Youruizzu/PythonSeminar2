# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input("Введите число: "))
two = 2
powtwo = int()
flag = True
while flag:
    for i in range(n):
        powtwo = two**i
        if powtwo < n:
            print(powtwo, f"(2 в степени {i})")
        else:
            flag = False
    flag = False
        