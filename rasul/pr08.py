# n = int(input("Введите число элементов списка: "))
# av = []
# for i in range (1,n + 1):
#     av.insert(i, int(input(f"Введите {i} число: ")))
# print(sum(av))

n = int(input("Введите число элементов списка: "))
av = []
fs = 0
for i in range (1,n + 1):
    l=int(input(f"Введите {i} число: "))
    av.append(l)
    fs+=l
print("Списoк: ", av)
print("Сумма: ",fs)
print("Среднее арифметическое:", fs/n)
print("Макс. значение: ", max(av))
print("Мин. значение: ", min(av))
pl = []
min = []
for n in av :
    if n>0:
        pl.append(n)
    else:
        min.append(n)
print("Вывод отрицатильных значений: ", min)
print("Вывод положительных значений: ", pl)
