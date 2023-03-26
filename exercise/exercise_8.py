# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество.
# Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

class Number_zeros:
    def __init__(self):
        self.numbers = []

    def count_zeros(self):
        count = 0
        for elem in self.numbers:
            if elem == 0:
                count += 1
        result = f'Количество нулей среди введенных чисел: {count}'
        return result

    def input_numbers(self):
        while True:
            try:
                count_numbers = int(input('Введите количество чисел: '))
                break
            except ValueError:
                print('Ошибка! Введите целое число.')
        for elem in range(count_numbers):
            while True:
                try:
                    number = int(input('Введите число: '))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print('Ошибка! Введите целое число.')

    def output_zerro(self):
        self.input_numbers()
        result = self.count_zeros()
        print(result)


numbers_zerro = Number_zeros()
numbers_zerro.output_zerro()
