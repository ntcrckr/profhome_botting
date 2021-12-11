# ООП - Объектно-ориентированное программирование
class MyClass:
    # Аттрибуты класса

    attr1 = 'first attribute'
    attr2 = 0

    # Методы класса. Задаются как функции
    def __init__(self, a, b, c):
        # Аттрибуты экземпляра класса. Определены только для конкретного экземпляра
        self._a1 = a
        self.b1 = b
        self.c1 = c
        self.attr2 += 1

    def my_method(self):
        return self._my_method2() + 1

    def _my_method2(self):
        return self._a1

    # Специальные методы. Ищите в гугле их смысл, если надо
    def __call__(self, x=1, y=1):
        return x * y

    def __str__(self):
        return 'My class'


def f(x: int, y: int, z: int = 10) -> int:
    return x + y - z


print(f(1, 1, 2.2))
print(f(1, 1))
x = MyClass(1, 2, 3)
print(x._a1)
# y = MyClass(3, 4, 5)
#
# print(x(10, 20))
# print(x())
# print(x)
