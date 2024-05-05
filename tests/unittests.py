import unittest
import pandas as pd
from notebooks.shared import handle_missing_values, date_to_datetime, standardize_text, handle_duplicates, save_processed_dataset


class TestNotebook(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame({
            'headline': ['This is a headline', 'Another headline', ''],
            'url': ['http://example.com', 'http://example.com', 'http://example.com'],
            'date': ['2022-01-01 10:00:00', '2022-02-02 11:00:00', '2022-03-03 12:00:00'],
            'stock': ['AAPL', 'GOOGL', 'MSFT'],
            'publisher': ['Publisher 1', 'Publisher 2', '']
        })

    def test_handle_missing_values(self):
        expected_output = pd.DataFrame({
            'headline': ['This is a headline', 'Another headline'],
            'url': ['http://example.com', 'http://example.com'],
            'date': ['2022-01-01 10:00:00', '2022-02-02 11:00:00'],
            'stock': ['AAPL', 'GOOGL'],
            'publisher': ['Publisher 1', 'Publisher 2']
        })

        output = handle_missing_values(self.df)
        pd.testing.assert_frame_equal(output, expected_output)

    def test_date_to_datetime(self):
        expected_output = pd.DataFrame({
            'headline': ['This is a headline', 'Another headline', ''],
            'url': ['http://example.com', 'http://example.com', 'http://example.com'],
            'date': ['2022-01-01 10:00:00', '2022-02-02 11:00:00', pd.NaT],
            'stock': ['AAPL', 'GOOGL', 'MSFT'],
            'publisher': ['Publisher 1', 'Publisher 2', '']
        })

        output = date_to_datetime(self.df)
        pd.testing.assert_frame_equal(output, expected_output)

    def test_standardize_text(self):
        expected_output = pd.DataFrame({
            'headline': ['headline', 'another headline', ''],
            'url': ['http://example.com', 'http://example.com', 'http://example.com'],
            'date': ['2022-01-01 10:00:00', '2022-02-02 11:00:00', '2022-03-03 12:00:00'],
            'stock': ['AAPL', 'GOOGL', 'MSFT'],
            'publisher': ['Publisher 1', 'Publisher 2', '']
        })

        output = standardize_text(self.df)
        pd.testing.assert_frame_equal(output, expected_output)

    def test_handle_duplicates(self):
        expected_output = pd.DataFrame({
            'headline': ['This is a headline', 'Another headline'],
            'url': ['http://example.com', 'http://example.com'],
            'date': ['2022-01-01 10:00:00', '2022-02-02 11:00:00'],
            'stock': ['AAPL', 'GOOGL'],
            'publisher': ['Publisher 1', 'Publisher 2']
        })

        output = handle_duplicates(self.df)
        pd.testing.assert_frame_equal(output, expected_output)

    def test_save_processed_dataset(self):
        output_folder = 'test_output'
        output_path = save_processed_dataset(self.df, output_folder)

        self.assertEqual(output_path, 'test_output/cleaned_analyst_ratings_dataset.csv')
        self.assertTrue(os.path.exists(output_path))

    def tearDown(self):
        # Clean up any temporary files or directories created during the tests
        pass


if __name__ == '__main__':
    unittest.main()