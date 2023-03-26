# Программа получает на вход последовательность целых неотрицательных чисел,
# каждое число записано в отдельной строке.
# Последовательность завершается числом 0, при считывании которого
# программа должна закончить свою работу и вывести количество
# членов последовательности (не считая завершающего числа 0).
# Числа, следующие за числом 0, считывать не нужно.

class Number_sequence_members:
    def __init__(self):
        self.sequence = []

    def input_sequence(self):
        while True:
            try:
                number = int(input('Введите число : '))
                if number == 0:
                    break
                self.sequence.append(number)
            except ValueError:
                print("Вы ввели неверный тип данных. Пожалуйста, введите целое число.")

    def count_members(self):
        return len(self.sequence)


number_sequence_members = Number_sequence_members()
number_sequence_members.input_sequence()
print(number_sequence_members.count_members())
