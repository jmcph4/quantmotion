from .ohlcvdata import OHLCVData
from .timeseries import TimeSeries
from .asset import Asset

class Portfolio(object):
    """
    Represents a collection of assets and a sequence of buying or selling events
    """
    def __init__(self, init=None, balance=None):
        if init is not None:
            self._holdings = deepcopy(init)
            self._initial = deepcopy(init)
        else:
            self._holdings = {}
            self._initial = None

        self._events = TimeSeries()

        if balance is not None:
            self._balance = balance
            self._initial_balance = balance
        else:
            self._balance = 0
            self._initial_balance = None

    @property
    def holdings(self):
        """
        P.holdings -- the current holdings of P
        """
        return self._holdings

    @property
    def balance(self):
        """
        P.balance -- the current cash balance of P
        """
        return self._balance

    def buy(self, asset, quantity, dt):
        """
        P.buy(asset, dt, quantity) -- buys quantity units of asset at dt

        Note that this will reduce the cash balance of the portfolio, while
        increasing the holding amount for the given asset
        """
        if asset not in self._holdings.keys():
            self._holdings[asset] = quantity
        else:
            self._holdings[asset] += quantity
        self._events[dt] = (asset, quantity)

    def sell(self, asset, quantity, dt):
        """
        P.sell(asset, dt, quantity) -- sells quantity units of asset at dt

        Note that this will increase the cash balance of the portfolio, while
        reducing the holding amount for the given asset
        """
        self._holdings[asset] -= quantity
        self._events[dt] = (asset, -1 * quantity)

    def value(self, dt):
        """
        P.value(dt) -- calculates the value of P at dt
        """
        if self._initial is not None:
            tally = deepcopy(self._initial)
        else:
            tally = {}

        if self._initial_balance is not None:
            bal = self._initial_balance
        else:
            bal = 0
            
        for key, event in self._events:
            asset = event[0]
            quantity = event[1]

            if quantity > 0: # buying
                if isinstance(asset.price_at(key), OHLCVData):
                    bal -= quantity * asset.price_at(key).close
                else:
                    bal -= quantity * asset.price_at(key)

                if asset not in tally.keys():
                    tally[asset] = quantity
                else:
                    tally[asset] += quantity
            else: # selling
                if isinstance(asset.price_at(key), OHLCVData):
                    bal += -1 * quantity * asset.price_at(key).close
                else:
                    bal += -1 * quantity * asset.price_at(key)

                tally[asset] -= -1 * quantity

                if tally[asset] == 0:
                    tally.pop(asset)

        holdings_value = 0

        for k, v in tally.items():
            if isinstance(k.price_at(dt), OHLCVData):
                holdings_value += k.price_at(dt).close * v
            else:
                holdings_value += k.price_at(dt) * v

        return holdings_value + bal

    def growth(self, start, end):
        a = self.value(start)
        b = self.value(end)

        return b / a
        
            
