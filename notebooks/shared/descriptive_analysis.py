import re
import matplotlib.pyplot as plt
import pandas as pd

def get_text_length_stats(data):
 
    headline_lengths = data['headline'].str.len()

    # Calculate statistics
    stats = {
        'mean': headline_lengths.mean(),
        'median': headline_lengths.median(),
        'minimum': headline_lengths.min(),
        'maximum': headline_lengths.max(),
        'standard_deviation': headline_lengths.std()
    }

    # Create a histogram
    plt.figure(figsize=(10, 6))
    plt.hist(headline_lengths, bins=20, color='steelblue', edgecolor='black')

    # Add labels and title
    plt.xlabel('Headline Length')
    plt.ylabel('Frequency')
    plt.title('Distribution of Headline Lengths')

    # Display the plot
    plt.show()

    return stats





def count_articles_per_publisher(data):
    publisher_counts = data['publisher'].value_counts()

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

    return publisher_counts
    



def identify_unique_domains(data):
    pattern = r'@(.*?)[\.\s]'
    data['domain'] = data['publisher'].apply(lambda x: re.findall(pattern, x)[0] if re.findall(pattern, x) else '')
    unique_domains = data['domain'].unique()
    return unique_domains




