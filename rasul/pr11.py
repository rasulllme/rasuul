# class Disciple:
#     def __init__(self, name, age, clas):
#         self.name = name
#         self.age = age
#         self.clas = clas
#     def print_Discipl(self):
#         print(f"Имя: {self.name}\tВозраст: {self.age}\tКласс:{self.clas}")
# bob = Disciple("Абулка", 16, 9)
# bob.print_Discipl()

# import message
# print(message.hello)
# message.print_message("Hello work")


# import os
#
# def get_words(filename):
#     with open(filename, encoding="utf8") as file:
#         text = file.read()
#     text = text.replace("\n"," ")
#     text =text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
#     text = text.lower()
#     words = text.split()
#     words.sort()
#     return words
# def get_words_dick(words):
#     words_dick = dict()
#     for word in words:
#         if word in words:
#             words_dick[word] = words_dick[word] + 1
#         else:
#             words_dick[word] = 1
#     return words_dick
#
#
# def main():
#     filename = input("Введите путь к файлу: ")
#     if not os.path.exists(filename):
#         print("Указанный файл не существует")
#     else:
#         words = get_words(filename)
#         words_dict = get_words_dick(words)
#         print(f"Кол-во слов: {len(words)}")
#         print(f"Кол-во уникальных слов: {len(words_dict)}")
#         print("Все использованные слова:")
#         for word in words_dict:
#             print(word.ljust(20), words_dict[word])
#
#
# if __name__ == "__main__":
#     main()

import random
from fileinput import filename

filename = input("Введите путь к файлу или имя")