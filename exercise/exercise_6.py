# Факториалом числа n называется произведение 1 × 2 × ... × n.
# Обозначение: n!.
# По данному натуральному n вычислите значение n!.
# Пользоваться математической библиотекой math в этой задаче запрещено.

class Factorial:
    def __init__(self, num=None):
        self.num = num

    def get_number(self):
        while True:
            try:
                self.num = int(input('Введите целое число: '))
                break
            except ValueError:
                print('Вы ввели некорректное значение. Попробуйте ещё раз.')

    def compute_factorial(self):
        if self.num is None:
            self.get_number()

        result = 1
        if self.num < 0:
            return None
        if self.num == 0:
            return 1
        for elem in range(1, self.num + 1):
            result *= elem
        return result


factorial = Factorial()
print(factorial.compute_factorial())
