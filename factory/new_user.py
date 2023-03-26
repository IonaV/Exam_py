# Создание пользователя
import random

class User:
    # Списки имён, фамилий и доменов почтовых сервисов
    names = ['John', 'Jane', 'Michael', 'Michelle', 'William', 'Anna', 'David', 'Maria', 'Robert', 'Susan']
    surnames = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Wilson', 'Davis', 'Garcia', 'Martinez', 'Anderson', 'Clark']
    email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'outlook.com', 'i.ua', 'ukr.net', 'mail.ua']
    upp_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = '1234567890'

    def __init__(self):
        self.email = self.email_random()
        self.username = self.username_random()
        self.password = self.password_random()

    def __str__(self):
        return self.email, self.username, self.password

    def email_random(self):
        # Случайным образом выбираем имя, фамилию и почтовый домен
        self.names = random.choice(self.names)
        self.surnames = random.choice(self.surnames)
        self.email_domains = random.choice(self.email_domains)

        # Генерируем случайное число для почтового адреса
        numbers = random.randint(100, 999)

        # Собираем и возвращаем случайный электронный адрес
        self.email = f"{self.names.lower()}.{self.surnames.lower()}{numbers}@{self.email_domains}"

        # Возврат значения
        return self.email

    def username_random(self):
        # Список всех символов, которые могут использоваться
        all_symbol = self.upp_letters + self.low_letters + self.digits

        # Генерируем случайную последовательность символов длиной 10
        self.username = ''.join(random.choice(all_symbol) for _ in range(10))

        # Возврат значения
        return self.username

    def password_random(self):
        # Список всех символов, которые могут использоваться
        all_symbols = self.upp_letters + self.low_letters + self.digits

        # Генерируем случайную длину пароля on 8 до 12 символов
        password_length = random.randint(8, 12)

        # Генерируем случайную последовательность символов длиной password_length
        self.password = ''.join(random.choice(all_symbols) for _ in range(password_length))

        # Возврат значения
        return self.password


if __name__ == '__main__':
    a = User()
    print(a.username, a.email, a.password)