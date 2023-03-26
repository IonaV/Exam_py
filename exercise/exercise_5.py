# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.

class First_digit_after_decimal:
    def __init__(self):
        while True:
            try:
                self.x = float(input("Введите положительное действительное число: "))
                if self.x > 0:
                    break
                else:
                    print("Число должно быть положительным.")
            except ValueError:
                print("Введите корректное число.")

    def find_first_digit(self):
        fractional_part = self.x - int(self.x)  # находим дробную часть числа
        first_digit = int(fractional_part * 10)  # находим первую цифру после десятичной точки
        return first_digit


first_digit_finder = First_digit_after_decimal()
first_digit = first_digit_finder.find_first_digit()
print("Первая цифра после десятичной точки в числе", first_digit_finder.x, ":", first_digit)

