# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

class Rearrange_adjacent:
    def __init__(self, lst):
        self.lst = lst

    def rearrange(self):
        for i in range(0, len(self.lst) - 1, 2):
            self.lst[i], self.lst[i + 1] = self.lst[i + 1], self.lst[i]

    def get_list(self):
        lst = []
        while True:
            try:
                n = int(input("Введите количество элементов списка: "))
                break
            except ValueError:
                print("Ошибка: введите целое число.")
        for i in range(n):
            while True:
                try:
                    x = int(input("Введите элемент списка: "))
                    break
                except ValueError:
                    print("Ошибка: введите целое число.")
            lst.append(x)
        return lst


lst = Rearrange_adjacent([]).get_list()
rearrange_adjacent = Rearrange_adjacent(lst)
rearrange_adjacent.rearrange()
print(lst)
