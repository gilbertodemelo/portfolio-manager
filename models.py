class Transaction:
    def __init__(self, **info):
        self.__date = info['DATE']
        self.__price = float(info['PRICE']) if info['PRICE'] != '' else float('nan')
        self.__description = info['DESCRIPTION']
        self.__amount = float(info['AMOUNT']) if info['AMOUNT'] != '' else float('nan')
        self.__quantity = float(info['QUANTITY']) if info['QUANTITY'] != '' else float('nan')

    def __str__(self):
        return f'Date: {self.__date} ' \
               f'Description: {self.__description} ' \
               f'Price: ${self.__price} ' \
               f'Quantity: {self.__quantity} ' \
               f'Amount: $ {self.__amount} '

    def __repr__(self):
        """Return a `repr(self`, a computer-readable string representation of this object. """
        return f"Transaction(date={self.__date!r}, description={self.__description!r}, price={self.__price!r}, " \
               f"quantity={self.__quantity!r}, amount={self.__amount!r})"


class Stock:
    def __init__(self, symbol):
        self.__symbol = symbol if len(symbol) > 0 else None
        self.__transactions = [] # a list of dictionaries of transactions

    @property
    def quantity(self):
        total_count  = 0
        for transaction in self.__transactions:
            quantity = transaction.__quantity
            description = transaction.__description
            amount = transaction.__amount
            if ("Bought" in description) and (amount < 0):
                total_count += quantity
            elif ("Sold" in description) and (amount > 0):
                total_count -= quantity
        return total_count
