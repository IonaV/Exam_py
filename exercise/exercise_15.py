# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.

class Various_elements:
    def __init__(self, list):
        self.list = list

    def count_various(self):
        count = 0
        prev_element = None

        for element in self.list:
            if element != prev_element:
                count += 1
                prev_element = element

        return count


list = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
various_elements = Various_elements(list)
print(various_elements.count_various())
