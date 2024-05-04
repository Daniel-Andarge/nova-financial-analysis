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
    return stats


def count_articles_per_publisher(data):
    publisher_counts = data['publisher'].value_counts()
    return publisher_counts
    

def identify_unique_domains(data):
    pattern = r'@(.*?)[\.\s]'
    data['domain'] = data['publisher'].apply(lambda x: re.findall(pattern, x)[0] if re.findall(pattern, x) else '')
    unique_domains = data['domain'].unique()
    return unique_domains




