import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np

def perform_sentiment_analysis(data):
    # Download the lexicon resource
    nltk.download('vader_lexicon')

    # Initialize the sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Perform sentiment analysis on each headline
    sentiment_scores = []
    for headline in data['headline']:
        # Handle NaN or None values
        if isinstance(headline, float) and np.isnan(headline):
            sentiment_scores.append(np.nan)
        else:
            # Convert headline to string
            headline_str = str(headline)
            # Calculate the compound score for the headline
            compound_score = sid.polarity_scores(headline_str)['compound']
            sentiment_scores.append(compound_score)

    # Add sentiment scores to the DataFrame
    data['sentiment_score'] = sentiment_scores

    return data