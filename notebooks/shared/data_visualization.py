import matplotlib.pyplot as plt
from textblob import TextBlob

def visualize_textual_lengths(data):
    lengths = data['headline'].str.len()
    # Create histogram to visualize the distribution of lengths
    plt.hist(lengths, bins=20)
    plt.xlabel('Textual Length')
    plt.ylabel('Frequency')
    plt.title('Distribution of Textual Lengths')
    plt.show()

def perform_sentiment_analysis(data):
    sentiment_scores = data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    # Create a bar plot to visualize sentiment scores
    plt.bar(data.index, sentiment_scores)
    plt.xlabel('Article Index')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Analysis of Headlines')
    plt.show()