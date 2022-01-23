import csv

from models import Transaction, Stock


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


def load_stocks(csv_path):
    transactions_list = load_transactions(csv_path)
    stocks_set = set()
    for transaction in transactions_list:
        my_stock = Stock(transaction.symbol)
        stocks_set.add(my_stock)
    return stocks_set













