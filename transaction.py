# Creates a transaction object from the data


class Transaction:
    def __init__(self, date, price, description, amount, quantity):
        self.__date = date
        self.__price = float(price)
        self.__description = description
        self.__amount = float(amount)
        self.__quantity = float(quantity)

    def __str__(self):
        return f'Date: {self.__date}' \
               f'Description: {self.__description}' \
               f'Price: ${self.__price}' \
               f'Quantity: {self.__quantity}' \
               f'Amount: $ {self.__amount}'

