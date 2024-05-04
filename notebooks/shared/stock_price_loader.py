import pandas as pd

import pandas as pd
import yfinance as yf


def fetch_stock_prices(ticker):
    # Fetch the historical stock price data using yfinance
    stock_data = yf.Ticker(ticker).history(period="max")
    
    # Return the fetched stock price data
    return stock_data




""" def load_stock_prices(df):
    # Load your dataset containing stock symbols and dates from a CSV file
   

    # Fetch and process stock data for each stock symbol
    for symbol in df['stock']:
        # Filter the dataset for the current stock symbol
        stock_df = df[df['stock'] == symbol]

        # Calculate the earliest and latest date for the current stock
        start_date = stock_df['date'].min()
        end_date = stock_df['date'].max()

        # Fetch stock data using yfinance
        stock_data = yf.download(symbol, start=start_date, end=end_date)

        # Process and analyze the fetched stock data as needed
        # ...

        # Example: Print the fetched stock data
        return stock_data """

