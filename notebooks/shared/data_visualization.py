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


