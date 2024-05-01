import re
import pandas as pd

def count_articles_per_publisher(data):
    article_counts = data['publisher'].value_counts()
    return article_counts

def analyze_publication_frequency(data):
    data['date'] = pd.to_datetime(data['date'])
    data['date'] = data['date'].dt.date
    publication_counts = data['date'].value_counts().sort_index()
    return publication_counts

def identify_unique_domains(data):
    pattern = r'@(.*?)[\.\s]'
    data['domain'] = data['publisher'].apply(lambda x: re.findall(pattern, x)[0])
    unique_domains = data['domain'].unique()
    return unique_domains