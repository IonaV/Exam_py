# Дано два числа a и b.
# Выведите гипотенузу треугольника с заданными катетами.

class Hypotenuse_triangle:
    def __init__(self):
        self.legs_1 = None
        self.legs_2 = None

    def input_legs(self):
        while True:
            try:
                self.legs_1 = float(input('Введите первый катет треугольника: '))
                self.legs_2 = float(input('Введите второй катет треугольника: '))
                break
            except ValueError:
                print('Ошибка: введите числовое значение')

    def calc_hypotenuse(self):
        result = f'Гипотенуза треугольника с заданными катетами: {(self.legs_1 ** 2 + self.legs_2 ** 2) ** 0.5}'
        return result


hypotenuse_triangle = Hypotenuse_triangle()
hypotenuse_triangle.input_legs()
print(hypotenuse_triangle.calc_hypotenuse())
