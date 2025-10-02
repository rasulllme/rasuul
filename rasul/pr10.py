from tkinter.font import names


# class Person:
#     pass
# class Person:
#     def __init__(self):
#         print("Создание обьекта Person")
# tom = Person()

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# bob = Person("bob", 22)
#
# print(bob.name)
# print(bob.age)
# bob.age = 37
# print(bob.age)

# class Student:
#     def __init__(self, name, age, well, group):
#         self.name = name
#         self.age = age
#         self.well = well
#         self.group = group
# Rasul = Student("Rasul", 16, 3, 32)
# Adil = Student("Adil", 18, 3, 32)
# print("Имя студента:", Rasul.name)
# print("Сколько лет:", Rasul.age)
# print("Курс студента:", Rasul.well)
# print("Группа студента: ", Rasul.group)
# print("Имя студента:", Adil.name)
# print("Сколько лет:", Adil.age)
# print("Курс студента:", Adil.well)
# print("Группа студента: ", Adil.group)
# print("Конец списка")


# class Rectangle:
#
#     def __init__(self, w, l):
#         self.width = w
#         self.length = l
#
#     def area(self):
#         return self.width * self.length
#
#     def perimeter(self):
#         return 2 * (self.width + self.length)
#
#
# rect1 = Rectangle(40, 40)
# print("rect1 area: ", rect1.area())
# print("rect1 perimeter: ", rect1.perimeter())
#
# rect2 = Rectangle(20, 30)
# print("rect2 area: ", rect2.area())
# print("rect2 perimeter: ", rect2.perimeter())
#
#
# class BankAccount:
#
#     def __init__(self, number, sum):
#         self.account_number = number
#         self.balance = sum
#         print(f"Создан счет. Начальный баланс: {sum} единиц")
#
#     def add(self, sum):
#         self.balance = self.balance + sum
#         print(f"На счет зачислено: {sum} единиц")
#
#     def withdraw(self, sum):
#         if self.balance >= sum:
#             self.balance = self.balance - sum
#             print(f"Со счета снято: {sum} единиц")
#         else:
#             print("Недостаточно средств на счете")
#
#
# acc1 = BankAccount("123456577", 1000)
# acc1.add(200)
# acc1.withdraw(500)
# acc1.withdraw(300)
# acc1.withdraw(900)

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_person(self):
        print(f"Имя: {self.name}\tВозраст: {self.age}")
tom = Person ("Tom", 39)
tom.__name = "Человек-паук"
tom.__age = -129
tom.print_person()