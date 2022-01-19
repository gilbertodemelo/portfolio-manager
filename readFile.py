import csv
import pprint


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


# Returns a list of transactions for the symbol
def get_transactions_for_symbol(transactions_dict: dict, symbol: str):
    result = list()
    for item in transactions_dict:
        if item == symbol:
            result.append(transactions_dict[symbol])
    return result


# Returns the current number of shares for the symbol
def get_number_of_shares(transactions_list: list):
    count = 0
    for item in transactions_list:
        for transaction in item:
            quantity = transaction["quantity"]
            amount = transaction["amount"]
            if (quantity != '') & (amount != ''):
                if (float(quantity) > 0) & (float(amount) < 0):
                    count += float(quantity)
                elif (float(quantity) > 0) & (float(amount) > 0):
                    count -= float(quantity)
    return count


def main():

    transactions_data = read_file('data/transactions.csv')
    transactions_symbols = get_list_of_symbols(transactions_data)
    result = get_transactions_structure(transactions_symbols, transactions_data)
    transactions_for_symbol = get_transactions_for_symbol(result, "AOA")
    pprint.pprint(transactions_for_symbol)


# Call main function
main()