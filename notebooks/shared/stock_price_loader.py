import yfinance as yf


def fetch_stock_prices(ticker):
    # Fetch stock price data using yfinance
    stock_data = yf.Ticker(ticker).history(period="max")

        # Reset the index
    stock_data = stock_data.reset_index()
    
    
    # Return the fetched stock price data
    return stock_data



