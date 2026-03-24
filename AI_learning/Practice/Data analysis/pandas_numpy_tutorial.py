#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pandas and NumPy Tutorial
-------------------------
This script demonstrates the key functionality of Pandas and NumPy libraries.
It covers data manipulation, analysis, and numerical operations.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# =============================================================================
# NUMPY TUTORIAL
# =============================================================================

def numpy_tutorial():
    print("\n" + "="*50)
    print("NUMPY TUTORIAL")
    print("="*50)
    
    # 1. Creating NumPy Arrays
    print("\n1. Creating NumPy Arrays:")
    # From Python lists
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"From list: {arr1}")
    
    # Using NumPy functions
    zeros = np.zeros(5)
    ones = np.ones(5)
    arange = np.arange(0, 10, 2)  # start, stop, step
    linspace = np.linspace(0, 1, 5)  # start, stop, num_points
    identity = np.eye(3)  # 3x3 identity matrix
    
    print(f"Zeros: {zeros}")
    print(f"Ones: {ones}")
    print(f"Arange: {arange}")
    print(f"Linspace: {linspace}")
    print(f"Identity matrix:\n{identity}")
    
    # 2. Array Operations
    print("\n2. Array Operations:")
    arr2 = np.array([10, 20, 30, 40, 50])
    
    # Basic arithmetic
    print(f"Addition: {arr1 + arr2}")
    print(f"Subtraction: {arr2 - arr1}")
    print(f"Multiplication: {arr1 * arr2}")
    print(f"Division: {arr2 / arr1}")
    print(f"Power: {arr1 ** 2}")
    
    # Statistical operations
    print(f"Mean: {np.mean(arr1)}")
    print(f"Sum: {np.sum(arr1)}")
    print(f"Min: {np.min(arr1)}")
    print(f"Max: {np.max(arr1)}")
    print(f"Standard deviation: {np.std(arr1)}")
    
    # 3. Reshaping Arrays
    print("\n3. Reshaping Arrays:")
    arr3 = np.arange(12)
    print(f"Original array: {arr3}")
    
    reshaped = arr3.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped}")
    
    # 4. Indexing and Slicing
    print("\n4. Indexing and Slicing:")
    print(f"First element: {arr3[0]}")
    print(f"Last element: {arr3[-1]}")
    print(f"First 5 elements: {arr3[:5]}")
    print(f"Elements from index 5 to end: {arr3[5:]}")
    print(f"Every other element: {arr3[::2]}")
    
    # 5. Boolean Indexing
    print("\n5. Boolean Indexing:")
    bool_mask = arr3 > 5
    print(f"Boolean mask: {bool_mask}")
    print(f"Elements where arr3 > 5: {arr3[bool_mask]}")
    
    # 6. Random Numbers
    print("\n6. Random Numbers:")
    random_ints = np.random.randint(1, 100, 5)
    random_floats = np.random.random(5)
    random_normal = np.random.normal(0, 1, 5)  # mean=0, std=1
    
    print(f"Random integers: {random_ints}")
    print(f"Random floats: {random_floats}")
    print(f"Random normal distribution: {random_normal}")
    
    # 7. Linear Algebra
    print("\n7. Linear Algebra:")
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    
    print(f"Matrix 1:\n{matrix1}")
    print(f"Matrix 2:\n{matrix2}")
    print(f"Matrix multiplication:\n{np.dot(matrix1, matrix2)}")
    print(f"Matrix transpose:\n{matrix1.T}")
    print(f"Matrix determinant: {np.linalg.det(matrix1)}")
    print(f"Matrix inverse:\n{np.linalg.inv(matrix1)}")
    
    # 8. Broadcasting
    print("\n8. Broadcasting:")
    arr4 = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr4}")
    print(f"Array + 10: {arr4 + 10}")  # Broadcasting scalar to array
    
    # 9. Saving and Loading Arrays
    print("\n9. Saving and Loading Arrays:")
    np.save('temp_array.npy', arr4)
    loaded_arr = np.load('temp_array.npy')
    print(f"Loaded array: {loaded_arr}")
    
    return "NumPy tutorial completed successfully!"

# =============================================================================
# PANDAS TUTORIAL
# =============================================================================

def pandas_tutorial():
    print("\n" + "="*50)
    print("PANDAS TUTORIAL")
    print("="*50)
    
    # 1. Creating DataFrames
    print("\n1. Creating DataFrames:")
    
    # From dictionary
    data = {
        'name': ['John', 'Anna', 'Peter', 'Linda'],
        'age': [28, 22, 35, 32],
        'city': ['New York', 'Paris', 'London', 'Tokyo'],
        'salary': [50000, 45000, 65000, 55000]
    }
    df = pd.DataFrame(data)
    print("DataFrame from dictionary:")
    print(df)
    
    # From NumPy array
    arr = np.random.rand(5, 3)
    df2 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
    print("\nDataFrame from NumPy array:")
    print(df2)
    
    # 2. Reading and Writing Data
    print("\n2. Reading and Writing Data:")
    
    # Save DataFrame to CSV
    df.to_csv('temp_data.csv', index=False)
    print("DataFrame saved to 'temp_data.csv'")
    
    # Read from CSV
    df_read = pd.read_csv('temp_data.csv')
    print("DataFrame read from 'temp_data.csv':")
    print(df_read)
    
    # 3. DataFrame Operations
    print("\n3. DataFrame Operations:")
    
    # Selecting columns
    print("Selecting columns:")
    print(df[['name', 'age']])
    
    # Filtering rows
    print("\nFiltering rows (age > 30):")
    print(df[df['age'] > 30])
    
    # Adding columns
    df['bonus'] = df['salary'] * 0.1
    print("\nAdding a new column 'bonus':")
    print(df)
    
    # Applying functions
    print("\nApplying functions (capitalize names):")
    print(df['name'].apply(lambda x: x.upper()))
    
    # 4. Data Aggregation
    print("\n4. Data Aggregation:")
    
    # Group by
    print("Group by 'city' and calculate mean salary:")
    print(df.groupby('city')['salary'].mean())
    
    # Pivot tables
    print("\nPivot table (average salary by city and age group):")
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 100], labels=['Young', 'Middle', 'Senior'])
    print(pd.pivot_table(df, values='salary', index='city', columns='age_group', aggfunc='mean'))
    
    # 5. Handling Missing Data
    print("\n5. Handling Missing Data:")
    
    # Create DataFrame with missing values
    df_missing = df.copy()
    df_missing.loc[0, 'age'] = np.nan
    df_missing.loc[1, 'salary'] = np.nan
    print("DataFrame with missing values:")
    print(df_missing)
    
    # Check for missing values
    print("\nCheck for missing values:")
    print(df_missing.isnull().sum())
    
    # Fill missing values
    print("\nFill missing values:")
    print(df_missing.fillna({'age': df_missing['age'].mean(), 'salary': df_missing['salary'].median()}))
    
    # Drop rows with missing values
    print("\nDrop rows with missing values:")
    print(df_missing.dropna())
    
    # 6. Time Series Data
    print("\n6. Time Series Data:")
    
    # Create date range
    dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
    print(f"Date range: {dates}")
    
    # Create time series
    ts = pd.Series(np.random.randn(5), index=dates)
    print("\nTime series:")
    print(ts)
    
    # Resampling
    print("\nResampling (weekly mean):")
    print(ts.resample('W').mean())
    
    # 7. Merging DataFrames
    print("\n7. Merging DataFrames:")
    
    # Create two DataFrames
    df1 = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['John', 'Anna', 'Peter', 'Linda']
    })
    
    df2 = pd.DataFrame({
        'id': [1, 2, 3, 5],
        'department': ['HR', 'Finance', 'IT', 'Marketing']
    })
    
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)
    
    # Merge DataFrames
    merged_df = pd.merge(df1, df2, on='id', how='inner')
    print("\nMerged DataFrame (inner join):")
    print(merged_df)
    
    # 8. Data Visualization with Pandas
    print("\n8. Data Visualization with Pandas:")
    
    # Create a larger dataset for visualization
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    data = {
        'date': dates,
        'value1': np.random.normal(100, 15, 100),
        'value2': np.random.normal(90, 10, 100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    }
    viz_df = pd.DataFrame(data)
    
    # Set the date as index
    viz_df.set_index('date', inplace=True)
    
    # Plot time series
    plt.figure(figsize=(10, 6))
    viz_df['value1'].plot(title='Time Series Plot')
    plt.savefig('time_series_plot.png')
    print("Time series plot saved as 'time_series_plot.png'")
    
    # Plot histogram
    plt.figure(figsize=(10, 6))
    viz_df['value1'].hist(bins=20)
    plt.title('Histogram')
    plt.savefig('histogram_plot.png')
    print("Histogram saved as 'histogram_plot.png'")
    
    # Plot box plot
    plt.figure(figsize=(10, 6))
    viz_df.boxplot(column=['value1', 'value2'])
    plt.title('Box Plot')
    plt.savefig('box_plot.png')
    print("Box plot saved as 'box_plot.png'")
    
    # 9. Advanced Operations
    print("\n9. Advanced Operations:")
    
    # Rolling window
    print("Rolling window (7-day mean):")
    print(viz_df['value1'].rolling(window=7).mean().head(10))
    
    # Expanding window
    print("\nExpanding window (cumulative mean):")
    print(viz_df['value1'].expanding().mean().head(10))
    
    # Pivot tables with aggregation
    print("\nPivot table with multiple aggregations:")
    print(pd.pivot_table(viz_df.reset_index(), 
                         values=['value1', 'value2'], 
                         index='category', 
                         aggfunc={'value1': ['mean', 'std'], 'value2': ['min', 'max']}))
    
    return "Pandas tutorial completed successfully!"

# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main():
    print("PANDAS AND NUMPY TUTORIAL")
    print("=========================")
    
    # Run NumPy tutorial
    numpy_result = numpy_tutorial()
    print(numpy_result)
    
    # Run Pandas tutorial
    pandas_result = pandas_tutorial()
    print(pandas_result)
    
    print("\nTutorial completed! Check the generated files for visualizations.")

if __name__ == "__main__":
    main() 