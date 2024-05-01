import pandas as pd
import string
import os

def date_to_datetime(df):
    df['date'] = pd.to_datetime(df['date'])
    return df

def handle_missing_values(df):
    # Check for missing values in any of the columns
    missing_values = df.isnull().sum()

    # Drop rows with empty headline, url, date, stock columns
    df = df.dropna(subset=['headline', 'url', 'date', 'stock'])

    # Replace empty row publisher column  with Unknown
    df['publisher'].fillna("Unknown", inplace=True)

    return df

def standardize_text(df):
    # Convert headline text to lowercase
    df['headline'] = df['headline'].str.lower()

    # Remove punctuation from the headline text
    df['headline'] = df['headline'].str.translate(str.maketrans('', '', string.punctuation))

    return df

def handle_duplicates(df):
    # Check for duplicate rows based on the url column
    duplicate_rows = df.duplicated(subset='url', keep=False)

    # Keep only the row with the latest date compared to all duplicate rows
    df = df[~duplicate_rows | (df['date'] == df[duplicate_rows]['date'].max())]

    return df


def save_processed_dataset(df, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Save the cleaned dataset
    output_path = os.path.join(output_folder, 'cleaned_analyst_ratings_dataset.csv')
    df.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to {output_path}")
    return output_path