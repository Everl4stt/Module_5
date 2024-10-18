class Point():

    def __init__(self, x, y):
        print("Создан объект класса ", self.__class__.__name__)
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def get(self):
        print("Координаты точки: x = ", self.x, " y = ", self.y)

    def set(self):
        self.x = float(input("Задайте координату x для точки "))
        self.y = float(input("Задайте координату y для точки "))

point1 = Point(5, 6)
point2 = Point(2, 3)
print("Первая точка")
point1.get()
print("Вторая точка")
point2.get()
print("Установить координаты второй точки")
point2.set()
point3 = point1 + point2
print("Координаты третьей точки после сложения point1 + point2")
point3.get()
print("Координаты третьей точки после умножения point1 * point2")
point3 = point1 * point2
point3.get()

