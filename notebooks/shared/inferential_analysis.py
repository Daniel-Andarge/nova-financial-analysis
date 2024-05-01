
import pandas as pd

from textblob import TextBlob
import matplotlib.pyplot as plt



def analyze_publication_dates(data):
    # Extract date components for analysis
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.dayofweek

    # Calculate news frequency by day of the week
    news_frequency = data.groupby('day')['headline'].count()
    print("News Frequency by Day of the Week:")
    print(news_frequency)

    # Calculate news frequency by month and year
    news_frequency_monthly = data.groupby(['year', 'month'])['headline'].count()
    print("News Frequency by Month and Year:")
    print(news_frequency_monthly)

    return [news_frequency, news_frequency_monthly]

    


""" def perform_sentiment_analysis(data):

    # Initialize sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")

    # Perform sentiment analysis on each headline
    sentiment_results = []
    for headline in data['headline']:
        sentiment = sentiment_pipeline(headline)[0]
        sentiment_results.append(sentiment)

    # Create a new column in the dataset for sentiment results
    data['sentiment'] = sentiment_results

    # Print the results
    print(data[['headline', 'sentiment']]) """



def perform_sentiment_analysis(data):
    # Calculate sentiment scores for each headline
    sentiment_scores = data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return sentiment_scores









