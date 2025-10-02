language = "russian"
if language == "english":
    print("Hello")
else:
    print("Привет")
print("End")

language = "german"
if language == "english":
    print("Hello")
    print("World")
elif language == "german":
    print("Hallo")
    print("Welt")
else:
    print("Привет")
    print("мир")
language = "german"
if language == "english":
        print("Hello")
elif language == "german":
        print("Hallo")
elif language == "french":
        print("Salut")
else:
        print("Привет")

# ввод года
y = 2024

# проверка года
if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    print("Год високосный")
else:
    print("Год не високосный")

y = 1990

# проверка года
if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    print("Год високосный")
else:
    print("Год не високосный")

a = 5
b = 6
if a>b :
    g=a
else:
    g=b
print(g)

number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")
print(f"number = {number}")
number += 1
message = "Hello"

for c in message:
    print(c)
app = ("Привеt")
for a in app:
    print(a)

for a in range(10):
    print(a, end=" ")

for n in range(4, 10):
    print(n, end=" ")
for n in range(0, 10, 2):
    print(n, end=" ")
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
for c1 in  "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")

number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, выходим из цикла
        break
    print(f"number = {number}")

