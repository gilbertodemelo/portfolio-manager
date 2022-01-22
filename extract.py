import csv


# the readFile function reads a .csv file and
# returns a list of transactions for the
# period
def read_file(file):
    transactions_data = []
    try:
        transactions_file = open(file)
        transactions_reader = csv.DictReader(transactions_file)
        transactions_data = list(transactions_reader)
    except IOError:
        print(IOError)
    return transactions_data


# Create a dictionary containing transaction
# symbols
def get_list_of_symbols(transactions_list):
    transactions_symbols = dict()
    for transaction in transactions_list:
        if transaction["SYMBOL"]:
            transactions_symbols[transaction["SYMBOL"]] = list()
    return transactions_symbols


def get_transactions_structure(symbols: dict, data: list):
    result = {}
    for item in symbols.keys():
        trans_list = []
        for transaction in data:
            if item == transaction["SYMBOL"]:
                trans_info = {"date":transaction["DATE"], "price": transaction["PRICE"],
                              "quantity": transaction["QUANTITY"], "description": transaction["DESCRIPTION"], "amount":transaction["AMOUNT"]}
                trans_list.append(trans_info)
                result[item] = trans_list
    return result








