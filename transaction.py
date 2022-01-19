# Creates a transaction object from the data


class Transaction:
    def __init__(self, date, price, description, quantity, amount):
        self.__date = date
        self.__price = price
        self.__description = description
        self.__amount = amount
        self.__quantity = quantity

    def __str__(self):
        return f'Date: {self.__date} ' \
               f'Description: {self.__description} ' \
               f'Price: ${self.__price} ' \
               f'Quantity: {self.__quantity} ' \
               f'Amount: $ {self.__amount} '

    def get_transaction_dictionary(self, date, price, description, quantity, amount):
        transaction_info = {'date': date, 'price': price, 'description': description, 'quantity': quantity, 'amount': amount}
        return transaction_info

