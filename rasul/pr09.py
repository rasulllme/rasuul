# a = int(input("Введите количество элементов списка: "))
# sp = []
# aw = 0
# for i in range(1, a + 1):
#     l = int(input(f"Введите {i} число: "))
#     sp.append(l)
#     aw+=l
# print("Ваш список:", sp)
# print("Сумма: ",aw)
# from itertools import count
#
# sp = []
# c = 0
# count = 0
# while True:
#     a = int(input("Введите число: "))
#     if a==0:
#         break
#     sp.append(a)
#     c+=a
#     count += 1
# print("Список", sp)
# print("При вводе 0 система останавлевается!")
# print("Ты ввел чисел: ", count)

# x = int(input("введи число: "))
# z = int(x)
# a=z//1000
# b=z%1000
# c=b//100
# d=z%100
# f=d//10
# u=z%10
# print(f"В числе {z}")
# print(f"тысяч {a}")
# print(f"Сотен {c}")
# print(f"Десяток {f}")
# print(f"Единицы {u}")

# myfile = open("hello.txt", "w")
with open(".txt", "w") as myfile:
    print("Работа в myfile")

open