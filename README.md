# QuantMotion #
---

QuantMotion is a Python 3 library assisting quantitative analysis of financial assets.

## Price Data ##
QuantMotion supports price formats common in the financial industry, for e.g. OHLC data from candlestick charts, OHLC bar charts, etc.

    from quantmotion.ohlcvdata import OHLCVData

    price = OHLCVData(open=1.00, high=2.00, low=0.50, close=1.33)


## Time Series ##
QuantMotion provides code for manipulating time series data, for instance:

	from datetime import datetime
    from quantmotion.timeseries import TimeSeries

    ts = TimeSeries()
	ts.insert(datetime(2018, 1, 1), OHLCVData(open=1.00, high=2.00, low=0.50, close=1.33))
	ts.insert(datetime(2018, 1, 1), OHLCVData(open=1.40, high=2.03, low=1.40, close=1.23))
	len(ts) # 2
	ts.remove(datetime(2018, 1, 1))
	len(ts) # 1

## File Format Support ##
QuantMotion supports common financial file formats. CSV is likely the most common:

	from quantmotion.timeseries import TimeSeries
	from quantmotion.convert import *

	with open("MSFT.csv", "r") as f:
		ts = convert_csv_to_time_series(f.read())

	len(ts) # 100

## Portfolio Backtesting ##
QuantMotion also supports rich portfolio management and backtesting facilities. These allow portfolios to be backtested on entirely custom data and allow for custom trading strategies to be backtested across different asset classes.

	from datetime import datetime
	from quantmotion.asset import Asset
    from quantmotion.portfolio import Portfolio

	# list of `Asset` objects
	assets = [MSFT, GOOG, APPL, WOW]
	
	# portfolio with initial cash balance of $50,000
	p = Portfolio(balance=50000)

	# trade on the portfolio
	p.buy(MSFT, 100, datetime(2018, 1, 1))
	p.buy(GOOG, 20, datetime(2017, 4, 5))
	p.sell(MSFT, 50, datetime(2018, 3, 5))

	# value the portfolio
	current_value = p.value(datetime(2018, 4, 28))
	growth = p.growth()
