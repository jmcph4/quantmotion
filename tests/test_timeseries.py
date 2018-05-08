import unittest
from datetime import datetime
from copy import deepcopy

from quantmotion.ohlcvdata import OHLCVData
from quantmotion.timeseries import TimeSeries


class TestTimeSeries(unittest.TestCase):
    __valid_initial_data = [
        [(datetime(2018, 1, 1), OHLCVData(1.00, 2.43, 0.52, 1.50, 100)),
         (datetime(2018, 1, 2), OHLCVData(2.00, 2.05, 1.95, 2.00, 5400))],
        [(datetime(2017, 1, 1), OHLCVData(4.50, 4.60, 2.40, 3.50, 567)),
         (datetime(2017, 1, 2), OHLCVData(3.50, 5.50, 2.30, 4.00, 900))]
                            ]
    __not_found_key = datetime(2001, 1, 1)
    __not_found_value = OHLCVData(-100, -200, -50, -120, -100)
    
    def test___init___normal(self):
        actual_ts = TimeSeries()

        expected_ts = TimeSeries()

        self.assertEqual(actual_ts, expected_ts)

    def test___init___initial_data(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])

        expected_ts = TimeSeries(init=self.__valid_initial_data[0])

        self.assertEqual(actual_ts, expected_ts)

    def test___getitem___normal(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])
        actual_item = actual_ts[self.__valid_initial_data[0][0][0]]

        expected_ts = TimeSeries(init=self.__valid_initial_data[0])
        expected_item = self.__valid_initial_data[0][0][1]
        
        self.assertEqual(actual_item, expected_item)
        self.assertEqual(len(actual_ts), len(expected_ts))

    def test___getitem___slice(self):
        ts = TimeSeries(init=self.__valid_initial_data[0])
        actual_ts = ts[self.__valid_initial_data[0][1][0]:]

        expected_ts = TimeSeries(init=self.__valid_initial_data[0][1:])

        self.assertEqual(actual_ts, expected_ts)

    def test___getitem___not_found(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])

        with self.assertRaises(KeyError):
            item = actual_ts[self.__not_found_key]

    def test___setitem___normal(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])
        actual_ts[self.__valid_initial_data[0][0][0]] = self.__valid_initial_data[0][1][1]

        self.assertEqual(actual_ts[self.__valid_initial_data[0][0][0]], self.__valid_initial_data[0][1][1])

    def test___setitem___not_found(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])
        actual_ts[self.__not_found_key] = self.__not_found_value

        data = deepcopy(self.__valid_initial_data[0])
        data.append((self.__not_found_key, self.__not_found_value))
        expected_ts = TimeSeries(init=data)

        self.assertEqual(actual_ts, expected_ts)

    def test___delitem___normal(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])
        del actual_ts[self.__valid_initial_data[0][0][0]]

        expected_ts = TimeSeries(init=self.__valid_initial_data[0][1:])

        self.assertEqual(actual_ts, expected_ts)

    def test___delitem___not_found(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])

        with self.assertRaises(KeyError):
            del actual_ts[self.__not_found_key]

    def test___eq___normal(self):
        a = TimeSeries(init=self.__valid_initial_data[0])
        b = TimeSeries(init=self.__valid_initial_data[0])

        self.assertTrue(a == b)

    def test___eq___unequal(self):
        a = TimeSeries(init=self.__valid_initial_data[0])
        b = TimeSeries(init=self.__valid_initial_data[1])

        self.assertFalse(a == b)

    def test___iter___normal(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])

        actual_items = []

        for k, v in actual_ts:
            actual_items.append((k, v))

        expected_items = deepcopy(self.__valid_initial_data[0])
        
        expected_ts = TimeSeries(init=expected_items)

        self.assertEqual(actual_items, expected_items)
        self.assertEqual(actual_ts, expected_ts)

    def test_insert_normal(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])
        actual_ts.insert(self.__not_found_key, self.__not_found_value)

        expected_values = deepcopy(self.__valid_initial_data[0])
        expected_values.append((self.__not_found_key, self.__not_found_value))

        expected_ts = TimeSeries(init=expected_values)

        self.assertEqual(actual_ts, expected_ts)

    def test_remove_normal(self):
        actual_ts = TimeSeries(init=self.__valid_initial_data[0])
        actual_ts.remove(self.__valid_initial_data[0][0][0])

        expected_ts = TimeSeries(init=self.__valid_initial_data[0][1:])

        self.assertEqual(actual_ts, expected_ts)

    def test___add___normal(self):
        a = TimeSeries(init=self.__valid_initial_data[0])
        b = TimeSeries(init=self.__valid_initial_data[1])
        c = a + b

        expected_ts = TimeSeries(init=self.__valid_initial_data[0] +
                              self.__valid_initial_data[1])

        self.assertEqual(c, expected_ts)

    def test___sub___normal(self):
        a = TimeSeries(init=self.__valid_initial_data[0])
        b = TimeSeries(init=self.__valid_initial_data[0])
        c = a - b

        expected_ts = TimeSeries()

        self.assertEqual(c, expected_ts)


if __name__ == "__main__":
    unittest.main()
