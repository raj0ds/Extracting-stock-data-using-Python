# Install yfinance module
!pip install yfinance

# Importing required modules
import yfinance as yf
import pandas as pd

# Using the Ticker module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is apple and the ticker symbol is APPL.
apple = yf.Ticker("AAPL")

# Using the attribute info we can extract information about the stock as a Python dictionary.
apple_info= apple.info
apple_info

# We can get the 'country' using the key country
apple_info['country']

# Using the history() method we can get the share price of the stock over a certain period of time. Using the period parameter we can set how far back from the present to get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
apple_share_price_data = apple.history(period="max")

# The format that the data is returned in is a Pandas DataFrame. With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
apple_share_price_data.head()

# We can reset the index of the DataFrame with the reset_index function. We also set the inplace paramter to True so the change takes place to the DataFrame itself.
apple_share_price_data.reset_index(inplace=True)

# We can plot the Open price against the Date:
apple_share_price_data.plot(x="Date", y="Open")

# Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns. Using the variable dividends we can get a dataframe of the data. The period of the data is given by the period defined in the 'history` function.
apple.dividends

# We can plot the dividends overtime:
apple.dividends.plot()
