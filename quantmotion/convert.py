from datetime import datetime
import csv
from io import StringIO

from .ohlcvdata import OHLCVData
from .timeseries import TimeSeries

DEFAULT_CSV_DELIMITER = ","
DEFAULT_CSV_QUOTE = '"'

def convert_csv_to_time_series(csv_data, dt_fmt):
    """
    convert_csv_to_time_series(csv_data) -- parse csv_data to TimeSeries type
    """
    csv_reader = csv.reader(StringIO(csv_data), delimiter=DEFAULT_CSV_DELIMITER, quotechar=DEFAULT_CSV_QUOTE)

    ts_data = []

    timestamp = 0
    open = 0
    high= 0
    low = 0
    close = 0
    volume = 0

    for row in csv_reader:
        for i in range(len(row)):
            if i == 0:
                timestamp = datetime.strptime(row[i], dt_fmt)
            elif i == 1:
                open = float(row[i])
            elif i == 2:
                high = float(row[i])
            elif i == 3:
                low = float(row[i])
            elif i == 4:
                close = float(row[i])
            elif i == 5:
                volume = float(row[i])

            entry = (timestamp, OHLCVData(open=open, high=high, low=low, close=close, volume=volume))
            ts_data.append(entry)

    return TimeSeries(init=ts_data)
