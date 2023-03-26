# Дана строка. Найдите в этой строке второе вхождение буквы f, и
# выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз, выведите число -1,
# а если не встречается # ни разу, выведите число -2.

class Occurrence_letter:
    def __init__(self):
        self.string = None

    def input_string(self):
        self.string = input("Введите строку: ")

    def occurrence_f(self):
        if not self.string:
            print("Строка не задана.")
            return
        first_occurrence = self.string.find('f')
        if first_occurrence == -1:
            return -2
        second_occurrence = self.string.find('f', first_occurrence + 1)
        if second_occurrence == -1:
            return -1
        return second_occurrence


occurrence_letter = Occurrence_letter()
occurrence_letter.input_string()
print(occurrence_letter.occurrence_f())
