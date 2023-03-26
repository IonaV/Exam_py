# Дано натуральное число.
# Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

class Leap_year_checker:
    def __init__(self):
        while True:
            try:
                self.year = int(input('Введите год: '))
                if self.year <= 0:
                    raise ValueError
                break
            except ValueError:
                print('Некорректный ввод. Пожалуйста, введите натуральное число.')

    def is_leap_year(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return True
        else:
            return False


checker = Leap_year_checker()
if checker.is_leap_year():
    print('YES')
else:
    print('NO')
