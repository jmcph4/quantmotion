from copy import deepcopy

class Asset(object):
    """
    Represents a generic asset
    """
    def __init__(self, name, prices):
        self._name = name
        self._prices = deepcopy(prices)

    @property
    def name(self):
        return self._name

    @property
    def prices(self):
        return self._prices

    def __repr__(self):
        return self._name

    def price_at(self, dt):
        """
        A.price_at(dt) -- returns the price of A at dt
        """
        return self._prices[dt]
    