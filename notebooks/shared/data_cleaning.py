import nltk
from nltk.corpus import stopwords
from dateutil import parser
import pandas as pd
import string
import os



def handle_missing_values(df):
    # Check for missing values in any of the columns
    missing_values = df.isnull().sum()

    # Drop the  row if one of the column value is empty for headline, url, date, stock columns
    df = df.dropna(subset=['headline', 'url', 'date', 'stock'], how='any')

    # Replace empty row publisher column with Unknown
    df.loc[:, 'publisher'] = df['publisher'].fillna("Unknown")

    return df


def date_to_datetime(df):
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    return df

def standardize_text(df):
    # Convert headline text to lowercase
    df['headline'] = df['headline'].str.lower()

    # Remove punctuation from the headline text
    df['headline'] = df['headline'].str.translate(str.maketrans('', '', string.punctuation))

    try:
        # Download stopwords if not already downloaded
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

    # Remove stopwords from the headline text
    stop_words = set(stopwords.words('english'))
    df['headline'] = df['headline'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

    return df


def handle_duplicates(df):
    duplicate_rows = df.duplicated(subset=['publisher', 'headline', 'url', 'stock'], keep=False)

    # Keep only the row with the latest date compared to all duplicate rows
    latest_dates = df.groupby(['publisher', 'headline', 'url', 'stock'])['date'].transform('max')
    df = df[~duplicate_rows | (df['date'] == latest_dates)]

    return df



def save_processed_dataset(df, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Apply handle_duplicates function to preprocess the dataset
    df_processed = handle_duplicates(df)

    # Save the cleaned dataset
    output_path = os.path.join(output_folder, 'cleaned_analyst_ratings_dataset.csv')
    df_processed.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to {output_path}")
    return output_path


