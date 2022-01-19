# Creates a transaction object from the data


class Transaction:
    def __init__(self, date, price, description, amount, quantity):
        self.__date = date
        self.__price = float(price)
        self.__description = description
        self.__amount = float(amount)
        self.__quantity = float(quantity)

    @property
    def amount(self):
        return self.__amount

    @property.setter
    def amount(self, amt):
        self.__amount = amt

    def __str__(self):
        return f'Date: {self.__date}' \
               f'Description: {self.__description}' \
               f'Price: ${self.__price}' \
               f'Quantity: {self.__quantity}' \
               f'Amount: $ {self.__amount}'

    def get_transaction_dictionary(self, date, price, description, amount, quantity):
        transaction_info = {'date': date, 'price': price, 'description': description, 'amount': amount, 'quantity': quantity}
        return transaction_info

