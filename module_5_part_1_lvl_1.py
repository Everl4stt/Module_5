class StringVar():
    def __init__(self, string1):
        self.string1 = string1

    def _get(self):
        print("Текущая строка: ", self.string1)

    def _set(self):
        self.string1 = input("Задайте строку\n")

str = StringVar("Привет")
str._get()
str._set()
str._get()