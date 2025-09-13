#Write a Python program to create a tool for generating synthetic data for testing purposes.
#Synthetic Data Generation Tool in Python

# Import necessary libraries
import pandas as pd
import numpy as np

class SyntheticDataGenerator:
    def __init__(self, num_rows, num_columns):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.data = None

    def generate_numeric_data(self, min_value=0, max_value=100):
        # Generate random numeric data
        self.data = pd.DataFrame(np.random.randint(min_value, max_value, size=(self.num_rows, self.num_columns)), columns=[f"Column_{i}" for i in range(1, self.num_columns + 1)])
    
    def generate_categorical_data(self, categories=None, weights=None):
        # Generate random categorical data
        if categories is None:
            categories = ['Category_A', 'Category_B', 'Category_C']
        if weights is None:
            weights = [0.5, 0.3, 0.2]
        self.data = pd.DataFrame(np.random.choice(categories, size=(self.num_rows, self.num_columns), p=weights), columns=[f"Column_{i}" for i in range(1, self.num_columns + 1)])
    
    def generate_dates(self, start_date='2020-01-01', end_date='2021-12-31', format='%Y-%m-%d'):
        # Generate date data
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        self.data = pd.DataFrame({'Date': pd.date_range(start=start_date, end=end_date, periods=self.num_rows)})
    
    def save_data(self, filename='synthetic_data.csv'):
        # Save generated data to a CSV file
        self.data.to_csv(filename, index=False)

# Example usage
if __name__ == "__main__":
    # Initialize data generator
    data_generator = SyntheticDataGenerator(num_rows=1000, num_columns=5)
    # Generate numeric data
    data_generator.generate_numeric_data()
    # Generate categorical data
    data_generator.generate_categorical_data()
    # Generate dates
    data_generator.generate_dates()
    # Save generated data to a CSV file
    data_generator.save_data('synthetic_data.csv')


