import pandas as pd

def align_datasets(sentiment_data, stock_price_data):
    sentiment_data['date'] = pd.to_datetime(sentiment_data['date'])
    stock_price_data['Date'] = pd.to_datetime(stock_price_data['Date'])

    sentiment_data.set_index('date', inplace=True)
    stock_price_data.set_index('Date', inplace=True)

    # Convert to timezone-aware indexes
    
    stock_price_data.index = stock_price_data.index.tz_localize('UTC')

    # Align datasets based on the date index
    aligned_data = sentiment_data.join(stock_price_data, how='inner')

    # Determine start and end dates for the aligned data
    start_date = max(aligned_data.index.min(), stock_price_data.index.min())
    end_date = min(aligned_data.index.max(), stock_price_data.index.max())

    # Filter the aligned data based on start and end dates
    aligned_data = aligned_data.loc[start_date:end_date]

    return aligned_data