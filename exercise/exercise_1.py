# Напишите программу, которая получает длины двух катетов в
# прямоугольном треугольнике и выводит его площадь.
# Каждое число записано в отдельной строке.

class Length_legs:
    def __init__(self, legs_1, legs_2):
        self.legs_1 = legs_1
        self.legs_2 = legs_2

    def area(self):
        result = f'Площадь прямоугольного треугольника по катетам: {0.5 * self.legs_1 * self.legs_2}'
        return result

    @classmethod
    def from_input(cls):
        while True:
            try:
                legs_1 = float(input('Введите длину первого катета: '))
                if legs_1 <= 0:
                    print('Длина катета должна быть положительным числом')
                    continue
                break
            except ValueError:
                print('Длина катета должна быть числом')

        while True:
            try:
                legs_2 = float(input('Введите длину второго катета: '))
                if legs_2 <= 0:
                    print('Длина катета должна быть положительным числом')
                    continue
                break
            except ValueError:
                print('Длина катета должна быть числом')

        return cls(legs_1, legs_2)


triangle = Length_legs.from_input()
print(triangle.area())
