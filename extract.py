import csv

from models import Transaction, Stock

# TODO: Remove last line (*** END OF FILE ***) from loading up.


def load_transactions(csv_path):
    transactions_collection = []
    try:
        with open(csv_path, 'r') as infile:
            reader = csv.DictReader(infile)
            for elem in reader:
                transactions_collection.append(Transaction(**elem))
    except IOError:
        print(IOError)
    return transactions_collection


# TODO: Make sure the same stock is not in the set more than once.
def load_stocks(csv_path):
    transactions_list = load_transactions(csv_path)
    stocks_symbols = set()
    stock_objs = set()
    for transaction in transactions_list:
        # my_stock = Stock(transaction.symbol)
        my_stock = transaction.symbol
        stocks_symbols.add(my_stock)

    for item in stocks_symbols:
        if item is not None:
            obj = Stock(item)
            stock_objs.add(obj)
    return stock_objs