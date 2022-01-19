# Creates a transaction object from the data


class Transaction:
    def __init__(self, date, price, description, amount, quantity):
        self.__date = date
        self.__price = float(price)
        self.__description = description
        self.__amount = float(amount)
        self.__quantity = float(quantity)