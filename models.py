from helpers import string_to_datetime


class Transaction:
    def __init__(self, **info):
        self.__date = string_to_datetime(info['DATE'])
        self.__price = float(info['PRICE']) if info['PRICE'] != '' else float('nan')
        self.__description = info['DESCRIPTION']
        self.__amount = float(info['AMOUNT']) if info['AMOUNT'] != '' else float('nan')
        self.__quantity = float(info['QUANTITY']) if info['QUANTITY'] != '' else float('nan')
        self.__symbol = info['SYMBOL'] if info['SYMBOL'] != '' else None

    @property
    def symbol(self):
        return self.__symbol

    @property
    def date(self):
        return self.__date

    def __str__(self):
        return f'Date: {self.__date} ' \
               f'Symbol: {self.__symbol} ' \
               f'Description: {self.__description} ' \
               f'Price: ${self.__price} ' \
               f'Quantity: {self.__quantity} ' \
               f'Amount: $ {self.__amount} '

    def __repr__(self):
        """Return a `repr(self`, a computer-readable string representation of this object. """
        return f"Transaction(date={self.__date!r}, symbol={self.__symbol!r} description={self.__description!r}, price={self.__price!r}, " \
               f"quantity={self.__quantity!r}, amount={self.__amount!r})"


class Stock:
    def __init__(self, symbol):
        self.__symbol = symbol if symbol != '' else None
        self.transactions = [] # a list of dictionaries of transactions

    @property
    def quantity(self):
        total_count = 0
        for transaction in self.transactions:
            quantity = transaction.quantity
            description = transaction.__description
            amount = transaction.__amount
            if ("Bought" in description) and (amount < 0):
                total_count += quantity
            elif ("Sold" in description) and (amount > 0):
                total_count -= quantity
        return total_count

    @property
    def symbol(self):
        return self.__symbol
