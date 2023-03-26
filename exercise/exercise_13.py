# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

class Element_greater_previous:
    def __init__(self):
        self.previous = 0
        self.count = 0

    def process_element(self, element):
        if element > self.previous:
            self.count += 1
        self.previous = element

    def get_result(self):
        return self.count


def main():
    element_greater_previous = Element_greater_previous()
    while True:
        try:
            element = int(input("Введите число: "))
            element_greater_previous.process_element(element)
        except ValueError:
            print("Ошибка: введите целое число.")
        else:
            if element == 0:
                break
    print("Количество элементов больше предыдущего:", element_greater_previous.get_result())


if __name__ == '__main__':
    main()
