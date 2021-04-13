import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd
import json
import csv


my_share = share.Share('ASML')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY, 10, share.FREQUENCY_TYPE_MINUTE, 5)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

csv_file = "test.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=symbol_data.keys())
        writer.writeheader()

        value_iterator = iter(symbol_data.values())

        
        timestamp_value = next(value_iterator)

        open_value = next(value_iterator)

        high_value = next(value_iterator)

        low_value = next(value_iterator)

        close_value = next(value_iterator)

        volume_value = next(value_iterator)

        for ts,o,h,l,c,v in zip(timestamp_value,open_value,high_value,low_value,close_value,volume_value):
            keys_iterator = iter(symbol_data.keys())
            writer.writerow(dict([(next(keys_iterator), ts), (next(keys_iterator), o), (next(keys_iterator), h), (next(keys_iterator), l), (next(keys_iterator), c), (next(keys_iterator), v)]))

except IOError:
    print("I/O error")
