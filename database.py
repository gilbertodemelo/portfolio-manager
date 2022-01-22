"""A database encapsulating collections of Stocks and their transactions """


class StockDatabase:
    """A database for stocks and their transactions.
    A `StockDatabase` contains a collection of Stocks and a collection of
    transactions.
    """
    def __init__(self, stocks, transactions):
        self.__stocks = stocks
        self.__transactions = transactions

    # TODO: Link together Stock objects and their transactions
        for stock in self.__stocks:
            symbol = stock.symbol
            transactions_list = []
            for transaction in self.__transactions:
                transac_symbol = transaction.symbol
                if symbol == transac_symbol:
                    transactions_list.append(transaction)
            stock.transactions = transactions_list