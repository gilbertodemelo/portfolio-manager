"""Converts datetimes to and from strings """

from datetime import datetime


# Returns a `datetime` corresponding to the given transaction date.
def string_to_datetime(transaction_date):
    return datetime.strptime(transaction_date, "%m/%d/%Y").date()


# Returns the date time as a human-readable string
def datetime_to_string(dt):
    return datetime.strptime(dt, "%m/%d/%Y")