class Person:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return f'{self.name}'


class Volunteer(Person):
    def __init__(self, name: str, city: str, status: str):
        super().__init__(name)
        self.city = city
        self.status = status
    def __str__(self):
        return f'"{self.name}", г.{self.city}, статус "{self.status}"'


clients =[]
clients.append(Volunteer('Иван Петров', 'Москва', 'Наставник'))
clients.append(Volunteer('Петр Иванов', 'Вятка', 'Тренер'))
clients.append(Volunteer('Василий Сидиров', 'Мытищи', 'Консультант'))
clients.append(Volunteer('Николай Лыков', 'Домодедово', 'Рядовой'))
clients.append(Volunteer('Василий Теркин', 'Курск', 'Рядовой'))
guests = []
for client in clients:
    if input(f"Приглашаем на корпоратив {client.name} ? (y/n)") == "y":
        guests.append(client)
for guest in guests:
    print(guest.__str__())
