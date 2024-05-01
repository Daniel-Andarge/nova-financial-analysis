import pandas as pd

def get_text_length_stats(data):
 
    headline_lengths = data['headline'].str.len()
    stats = {
        'mean': headline_lengths.mean(),
        'median': headline_lengths.median(),
        'minimum': headline_lengths.min(),
        'maximum': headline_lengths.max(),
        'standard_deviation': headline_lengths.std()
    }
    return stats

def count_articles_per_publisher(data):

    publisher_counts = data['publisher'].value_counts()
    return publisher_counts