import pandas as pd

def align_datasets(sentiment_data, stock_price_data):

    sentiment_data['date'] = pd.to_datetime(sentiment_data['date'])
    stock_price_data['Date'] = pd.to_datetime(stock_price_data['Date'])

    sentiment_data.set_index('date', inplace=True)
    stock_price_data.set_index('Date', inplace=True)

    # Align datasets based on the date index
    aligned_data = sentiment_data.join(stock_price_data, how='inner')

    


    return aligned_data