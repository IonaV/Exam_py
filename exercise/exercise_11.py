# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
# При решении этой задачи не стоит пользоваться циклами и инструкцией if.

class Permutation_words:
    def __init__(self):
        self.string = ""

    def get_string(self):
        while True:
            string = input('Введите строку из двух слов разделенных пробелом : ')
            if isinstance(string, str) and len(string.split()) == 2:
                self.string = string
                break
            else:
                print("Неверный формат строки. Попробуйте еще раз.")

    def Perm_words(self):
        words = self.string.split()
        words.reverse()
        return ' '.join(words)


permutation_words = Permutation_words()
permutation_words.get_string()
print(permutation_words.Perm_words())
