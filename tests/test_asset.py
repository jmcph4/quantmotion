import unittest
from datetime import datetime

from quantmotion.ohlcvdata import OHLCVData
from quantmotion.timeseries import TimeSeries
from quantmotion.asset import Asset


class TestAsset(unittest.TestCase):
    __valid_asset_name = "Tulips"
    __valid_ts_data = [(datetime(2018, 1, 1),
                        OHLCVData(1.00, 2.43, 0.52, 1.50, 100)),
         (datetime(2018, 1, 2), OHLCVData(2.00, 2.05, 1.95, 2.00, 5400))]

    __valid_asset_prices = TimeSeries(init=__valid_ts_data)

    def test___init___normal(self):
        actual_asset = Asset(self.__valid_asset_name, self.__valid_asset_prices)

        expected_asset = Asset(self.__valid_asset_name,
                               self.__valid_asset_prices)

        self.assertEqual(actual_asset, expected_asset)

    def test_name_normal(self):
        asset = Asset(self.__valid_asset_name, self.__valid_asset_prices)
        actual_name = asset.name

        expected_name = self.__valid_asset_name

        self.assertEqual(actual_name, expected_name)

    def test_prices_normal(self):
        asset = Asset(self.__valid_asset_name, self.__valid_asset_prices)
        actual_prices = asset.prices

        expected_prices = self.__valid_asset_prices

    def test___repr___normal(self):
        asset = Asset(self.__valid_asset_name, self.__valid_asset_prices)
        actual_representation = repr(asset)

        expected_representation = self.__valid_asset_name

        self.assertEqual(actual_representation, expected_representation)

    def test_price_at_normal(self):
        asset = Asset(self.__valid_asset_name, self.__valid_asset_prices)
        actual_price = asset.price_at(datetime(2018, 1, 2))

        expected_price = self.__valid_asset_prices[datetime(2018, 1, 2)]

        self.assertEqual(actual_price, expected_price)

if __name__ == "__main__":
    unittest.main()