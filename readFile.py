import csv
import pprint


def main():

    transactionsFile = open('transactions.csv')
    transactionsReader = csv.DictReader(transactionsFile)
    transactionsData = list(transactionsReader)

    #print(transactionsData)

    transactions_symbols = dict()
    transaction_list = list()
    # Create dictionary containing transaction symbols
    for transaction in transactionsData:
        if transaction["SYMBOL"]:
            transactions_symbols[transaction["SYMBOL"]] = transaction_list.append(transaction)

    result = {}
    for item in transactions_symbols.keys():
        trans_list = []
        for transaction in transactionsData:
            if item == transaction["SYMBOL"]:
                trans_info = {"date":transaction["DATE"], "price":transaction["PRICE"], "quantity":transaction["QUANTITY"], "description":transaction["DESCRIPTION"], "amount":transaction["AMOUNT"]}
                trans_list.append(trans_info)
                result[item] = trans_list


    pprint.pprint(result)


# Call main function
main()