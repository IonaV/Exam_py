# Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2
# (если два совпадает) или 0 (если все числа различны).

class Three_integers:
    def __init__(self):
        self.num_1 = 0
        self.num_2 = 0
        self.num_3 = 0

    def input_numbers(self):
        while True:
            try:
                self.num_1 = int(input('Введите первое целое число: '))
                self.num_2 = int(input('Введите второе целое число: '))
                self.num_3 = int(input('Введите третье целое число: '))
                break
            except ValueError:
                print('Ошибка: введите только целые числа.')
                continue

    def coincidence(self):
        if self.num_1 == self.num_2 == self.num_3:
            return 'Cовпадают 3 числа.'
        elif self.num_1 == self.num_2 or self.num_1 == self.num_3 or self.num_2 == self.num_3:
            return 'Cовпадают 2 числа.'
        else:
            return 'Числа различны 0.'


three_integers = Three_integers()
three_integers.input_numbers()
print(three_integers.coincidence())
