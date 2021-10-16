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

def get_list_of_symbols(transactions_list):
    transactions_symbols = dict()
    # Create a dictionary containing transaction
    #symbols
    for transaction in transactions_list:
        if transaction["SYMBOL"]:
            transactions_symbols[transaction["SYMBOL"]] = list()
    return transactions_symbols
#

def main():

    transactions_data = read_file('transactions.csv')

    transactions_symbols = get_list_of_symbols(transactions_data)


    result = {}
    for item in transactions_symbols.keys():
        trans_list = []
        for transaction in transactions_data:
            if item == transaction["SYMBOL"]:
                trans_info = {"date":transaction["DATE"], "price":transaction["PRICE"], "quantity":transaction["QUANTITY"], "description":transaction["DESCRIPTION"], "amount":transaction["AMOUNT"]}
                trans_list.append(trans_info)
                result[item] = trans_list

    pprint.pprint(result)


# Call main function
main()