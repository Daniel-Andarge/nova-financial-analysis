import pandas as pd
import yfinance as yf
import talib

def load_stock_prices(df):
    processed_data = pd.DataFrame()  # Initialize an empty dataframe for processed data

    # Fetch and process stock data for each stock symbol
    for symbol in df['stock']:
        # Filter the dataset for the current stock symbol
        stock_df = df[df['stock'] == symbol]

        # Calculate the earliest and latest date for the current stock
        start_date = stock_df['date'].min()
        end_date = stock_df['date'].max()

        # Fetch stock data using yfinance
        stock_data = fetch_stock_data(symbol, start_date, end_date)

        # Calculate technical indicators using TA-Lib
        stock_data = calculate_technical_indicators(stock_data)

        # Concatenate processed data to the main dataframe
        processed_data = pd.concat([processed_data, stock_data])

    return processed_data

def fetch_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def calculate_technical_indicators(stock_data):
    # Calculate moving averages
    stock_data['MA_10'] = talib.SMA(stock_data['Close'], timeperiod=10)
    stock_data['MA_20'] = talib.SMA(stock_data['Close'], timeperiod=20)

    # Calculate RSI (Relative Strength Index)
    stock_data['RSI'] = talib.RSI(stock_data['Close'])

    # Calculate MACD (Moving Average Convergence Divergence)
    macd, signal, _ = talib.MACD(stock_data['Close'])
    stock_data['MACD'] = macd
    stock_data['Signal'] = signal

    return stock_data