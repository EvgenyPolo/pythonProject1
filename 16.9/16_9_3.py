class User:
    def __init__(self, name, money=0):
        self.name = name
        self.balance = money


ivan = User("Иван Петров", 50)
print(f'Клиент "{ivan.name}". Баланс: {ivan.balance} руб.')


