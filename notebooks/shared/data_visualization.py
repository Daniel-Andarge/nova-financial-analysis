import matplotlib.pyplot as plt
from textblob import TextBlob
import seaborn as sns
import numpy as np
import yfinance as yf

def plot_text_length_stats(stats):
    # Extract the statistic values
    values = [stats['mean'], stats['median'], stats['minimum'], stats['maximum'], stats['standard_deviation']]
    labels = ['Mean', 'Median', 'Minimum', 'Maximum', 'Standard Deviation']

    # Create a bar plot
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color='steelblue')

    # Add labels and title
    plt.xlabel('Statistic')
    plt.ylabel('Headline Length')
    plt.title('Descriptive Analysis of Headline Lengths')

    # Display the plot
    plt.show()



def plot_publisher_counts(publisher_counts):
    # Select only the top ten publishers by count
    top_publishers = publisher_counts[:50]

    # Create a bar chart
    plt.figure(figsize=(12, 6))
    ax = top_publishers.plot(kind='bar', color='steelblue')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Customize the x-axis labels
    plt.xticks(rotation=45, ha='right')

    # Add labels and title
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.title('Number of Articles per Top 50 Publishers')

    # Display the plot
    plt.tight_layout()
    plt.show()



def visualize_publication_dates(news_frequency, news_frequency_monthly):
    # Reset index for news_frequency_monthly DataFrame
    news_frequency_monthly = news_frequency_monthly.reset_index()

    # Create a line chart for news frequency by day of the week
    plt.figure(figsize=(8, 6))
    plt.plot(news_frequency.index, news_frequency.values, marker='o', linestyle='-', color='steelblue')

    # Add labels and title for the line chart
    plt.xlabel('Day of the Week')
    plt.ylabel('News Frequency')
    plt.title('News Frequency by Day of the Week')

    # Customize x-axis tick labels
    day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.xticks(range(7), day_labels)

    # Display the line chart for news frequency by day of the week
    plt.show()

    # Create a line chart for news frequency by month and year
    plt.figure(figsize=(10, 6))
    plt.plot(news_frequency_monthly.index, news_frequency_monthly['headline'], marker='o', linestyle='-', color='steelblue')

    # Add labels and title for the line chart
    plt.xlabel('Month and Year')
    plt.ylabel('News Frequency')
    plt.title('News Frequency by Month and Year')

    # Display the line chart for news frequency by month and year
    plt.show()

    

def plot_domain_frequency(data):

    # Count frequency of each domain
    domain_counts = data['domain'].value_counts()
    # Exclude empty domain ('')
    domain_counts = domain_counts[1:]
    # Plot bar chart
    plt.bar(domain_counts.index, domain_counts.values)
    plt.xlabel('Domains')
    plt.ylabel('Frequency')
    plt.title('Frequency of Unique Domains in Headlines')
    plt.xticks(rotation=45)
    plt.show()





def visualize_stock_prices(stock_data, ticker):
    # Fetch the company name using the ticker
    ticker_info = yf.Ticker(ticker)
    company_name = ticker_info.info['longName']

    # Plot the closing prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'])
    plt.title(f"Historical Stock Prices for {company_name} ({ticker})")
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.grid(True)
    plt.show()