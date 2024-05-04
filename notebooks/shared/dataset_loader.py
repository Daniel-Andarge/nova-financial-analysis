import pandas as pd
import os
import sys

def load_raw_dataset():
    try:
        # Get the path to the CSV file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, '../data/raw_analyst_ratings.csv')

        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_path)

        return df
    except FileNotFoundError as e:
        print(f"Error: {e}. The dataset file was not found.")
    except Exception as e:
        print(f"Error: {e}. An error occurred while loading the dataset.")

    return None


def load_cleaned_dataset():
    try:
        # Get the path to the CSV file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, '../data/cleaned_analyst_ratings_dataset.csv')

        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_path)

        return df
    except FileNotFoundError as e:
        print(f"Error: {e}. The dataset file was not found.")
    except Exception as e:
        print(f"Error: {e}. An error occurred while loading the dataset.")

    return None


