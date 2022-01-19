# Stock with a list of transactions

class Stock:
    def __init__(self, symbol):
        self.__symbol = symbol
        self.__transactions = []

    def show_transactions(self):
        for item in self.__transactions:
            key, value = item.items()
            print(f'{key} : {value}\n')
