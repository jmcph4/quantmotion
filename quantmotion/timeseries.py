from collections import OrderedDict
from copy import deepcopy

from .ohlcvdata import OHLCVData

class TimeSeries(object):
    """
    Represents a time series
    """
    def __init__(self, init=None):
        if init is not None:
            self._data = OrderedDict(deepcopy(init))
        else:
            self._data = OrderedDict()

    def __getitem__(self, key):
        if isinstance(key, slice): # handle slicing
            keys_list = list(self._data.keys())

            start = 0
            stop = 0

            if key.start is not None and key.stop is not None:
                start = keys_list.index(key.start)
                stop = keys_list.index(key.stop)
            elif key.start is not None:
                start = keys_list.index(key.start)
                stop = len(keys_list)
            elif key.stop is not None:
                start = 0
                stop = keys_list.index(key.stop)
            else:
                start = 0
                stop = len(keys_list)

            sliced_keys = [keys_list[i] for i in range(start, stop)]

            ts = TimeSeries()

            for sk in sliced_keys:
                ts._data[sk] = self._data[sk]

            return ts
            
        else: # regular access
            return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        self._data.pop(key)

    def __eq__(self, o):
        if isinstance(o, type(self)):
            if self._data == o._data:
                return True
            else:
                return False
        else:
            return False

    def __iter__(self):
        return ((k, v) for k, v in self._data.items())

    def insert(self, key, value):
        """
        TS.insert(key, value) -- inserts value and associates it with key
        """
        self._data[key] = value

    def remove(self, key):
        """
        TS.remove(key) -- removes the value associated with key
        """
        if key in self._data.keys():
            self._data.pop(key)
        else:
            raise KeyError()
            
    def __len__(self):
        return len(self._data)
    
    def __add__(self, o):
        if isinstance(o, type(self)):
            return self._concatenate(o)
        else:
            raise TypeError()

    def __sub__(self, o):
        if isinstance(o, type(self)):
            return self._remove_keys(o._data.keys())
        else:
            raise TypeError()

    def keys(self):
        return sorted(self._data.keys())

    def _concatenate(self, ts):
        a = self._ordereddict_to_list(self._data)
        b = self._ordereddict_to_list(ts._data)

        return TimeSeries(init=a + b)

    def _ordereddict_to_list(self, od):
        l = []
        
        for k, v in od.items():
            l.append((k, v))

        return l

    def _remove_keys(self, keys):
        ts = deepcopy(self)
    
        for k in keys:
            ts._data.pop(k)

        return ts

    def __repr__(self):
        s = ""

        for k, v in self._data.items():
            s += str(k) + ": " + str(v) + "\n"

        return s

    
