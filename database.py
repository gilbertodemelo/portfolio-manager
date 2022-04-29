"""A database encapsulating collections of Stocks and their transactions """
import math


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

    def get_transactions_by_symbol(self, symbol: str) -> dict:
        """Find a stock and its transactions by its symbol. """
        result = dict()
        for stock in self.__stocks:
            #sorted_transactions = sorted(stock.transactions, key=lambda d: d.date)
            if stock.symbol == symbol:
                stock.transactions.sort(key=lambda d: d.date)
                result[symbol] = stock.transactions
        return result

    def get_current_quantity(self, symbol: str):
        count: int = 0
        stock_dict = self.get_transactions_by_symbol(symbol)
        for transaction in stock_dict[symbol]:
            if ('Bought' in transaction.description) and not (math.isnan(transaction.quantity)):
                if transaction.quantity >= 1:
                    count += transaction.quantity
            elif ('Sold' in transaction.description) and not (math.isnan(transaction.quantity)):
                if transaction.quantity >= 1:
                    count -= transaction.quantity
        return count



    @property
    def stocks(self):
        return self.__stocks
