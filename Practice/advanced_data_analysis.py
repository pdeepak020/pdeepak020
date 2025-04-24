#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advanced Data Analysis with Pandas and NumPy
-------------------------------------------
This script demonstrates advanced data analysis techniques using Pandas and NumPy.
It includes data preprocessing, feature engineering, and basic machine learning concepts.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

# =============================================================================
# DATA GENERATION AND PREPROCESSING
# =============================================================================

def generate_sample_data(n_samples=1000):
    """
    Generate a synthetic dataset for demonstration purposes.
    """
    print("Generating synthetic dataset...")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate features
    age = np.random.normal(35, 10, n_samples)
    income = np.random.normal(50000, 20000, n_samples)
    education_years = np.random.normal(15, 3, n_samples)
    work_experience = np.random.normal(10, 5, n_samples)
    
    # Generate categorical features
    education_level = np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_samples, p=[0.3, 0.4, 0.2, 0.1])
    occupation = np.random.choice(['Tech', 'Finance', 'Healthcare', 'Education', 'Other'], n_samples, p=[0.3, 0.2, 0.2, 0.1, 0.2])
    city = np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], n_samples, p=[0.3, 0.25, 0.2, 0.15, 0.1])
    
    # Generate target variables
    # Salary prediction (regression)
    salary = 20000 + 1000 * education_years + 500 * work_experience + 0.05 * income + np.random.normal(0, 5000, n_samples)
    
    # Job satisfaction (classification)
    satisfaction_score = 0.3 * education_years + 0.2 * work_experience + 0.1 * income / 10000 + np.random.normal(0, 1, n_samples)
    job_satisfaction = (satisfaction_score > 0).astype(int)
    
    # Create DataFrame
    data = {
        'age': age,
        'income': income,
        'education_years': education_years,
        'work_experience': work_experience,
        'education_level': education_level,
        'occupation': occupation,
        'city': city,
        'salary': salary,
        'job_satisfaction': job_satisfaction
    }
    
    df = pd.DataFrame(data)
    
    # Add some missing values
    df.loc[np.random.choice(df.index, 50), 'income'] = np.nan
    df.loc[np.random.choice(df.index, 30), 'education_years'] = np.nan
    
    # Add some outliers
    df.loc[np.random.choice(df.index, 10), 'salary'] = df.loc[np.random.choice(df.index, 10), 'salary'] * 3
    
    print(f"Generated dataset with {n_samples} samples and {len(df.columns)} features.")
    return df

# =============================================================================
# EXPLORATORY DATA ANALYSIS
# =============================================================================

def exploratory_data_analysis(df):
    """
    Perform exploratory data analysis on the dataset.
    """
    print("\n" + "="*50)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*50)
    
    # 1. Basic Information
    print("\n1. Basic Information:")
    print(f"Dataset shape: {df.shape}")
    print("\nData types:")
    print(df.dtypes)
    
    # 2. Summary Statistics
    print("\n2. Summary Statistics:")
    print(df.describe())
    
    # 3. Missing Values
    print("\n3. Missing Values:")
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Values': missing_values,
        'Percentage': missing_percentage
    })
    print(missing_df[missing_df['Missing Values'] > 0])
    
    # 4. Correlation Analysis
    print("\n4. Correlation Analysis:")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    correlation = df[numeric_cols].corr()
    print(correlation)
    
    # 5. Visualizations
    print("\n5. Visualizations:")
    
    # Histogram of numeric features
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(2, 4, i)
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
    plt.tight_layout()
    plt.savefig('numeric_distributions.png')
    print("Numeric distributions saved as 'numeric_distributions.png'")
    
    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    print("Correlation heatmap saved as 'correlation_heatmap.png'")
    
    # Box plots for categorical features
    categorical_cols = df.select_dtypes(include=['object']).columns
    for cat_col in categorical_cols:
        plt.figure(figsize=(12, 6))
        sns.boxplot(x=cat_col, y='salary', data=df)
        plt.title(f'Salary by {cat_col}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'salary_by_{cat_col.lower()}.png')
        print(f"Salary by {cat_col} saved as 'salary_by_{cat_col.lower()}.png'")
    
    return "Exploratory data analysis completed successfully!"

# =============================================================================
# DATA PREPROCESSING
# =============================================================================

def preprocess_data(df):
    """
    Preprocess the dataset for machine learning.
    """
    print("\n" + "="*50)
    print("DATA PREPROCESSING")
    print("="*50)
    
    # 1. Handle Missing Values
    print("\n1. Handling Missing Values:")
    
    # Check missing values before preprocessing
    missing_before = df.isnull().sum().sum()
    print(f"Total missing values before preprocessing: {missing_before}")
    
    # Fill missing values
    df_processed = df.copy()
    
    # Fill numeric missing values with median
    numeric_cols = df_processed.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_cols:
        df_processed[col].fillna(df_processed[col].median(), inplace=True)
    
    # Fill categorical missing values with mode
    categorical_cols = df_processed.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df_processed[col].fillna(df_processed[col].mode()[0], inplace=True)
    
    # Check missing values after preprocessing
    missing_after = df_processed.isnull().sum().sum()
    print(f"Total missing values after preprocessing: {missing_after}")
    
    # 2. Handle Outliers
    print("\n2. Handling Outliers:")
    
    # Detect outliers using IQR method
    for col in numeric_cols:
        Q1 = df_processed[col].quantile(0.25)
        Q3 = df_processed[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df_processed[(df_processed[col] < lower_bound) | (df_processed[col] > upper_bound)][col]
        print(f"Number of outliers in {col}: {len(outliers)}")
    
    # Cap outliers
    for col in numeric_cols:
        Q1 = df_processed[col].quantile(0.25)
        Q3 = df_processed[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_processed[col] = df_processed[col].clip(lower_bound, upper_bound)
    
    # 3. Feature Engineering
    print("\n3. Feature Engineering:")
    
    # Create interaction features
    df_processed['education_income'] = df_processed['education_years'] * df_processed['income'] / 10000
    df_processed['experience_income'] = df_processed['work_experience'] * df_processed['income'] / 10000
    
    # Create polynomial features
    df_processed['age_squared'] = df_processed['age'] ** 2
    df_processed['education_squared'] = df_processed['education_years'] ** 2
    
    # Create binary features
    df_processed['high_education'] = (df_processed['education_level'].isin(['Master', 'PhD'])).astype(int)
    df_processed['high_income'] = (df_processed['income'] > df_processed['income'].median()).astype(int)
    
    # 4. Encoding Categorical Variables
    print("\n4. Encoding Categorical Variables:")
    
    # One-hot encoding
    categorical_cols = df_processed.select_dtypes(include=['object']).columns
    df_encoded = pd.get_dummies(df_processed, columns=categorical_cols, drop_first=True)
    
    print(f"Original number of features: {len(df_processed.columns)}")
    print(f"Number of features after encoding: {len(df_encoded.columns)}")
    
    return df_encoded

# =============================================================================
# MACHINE LEARNING
# =============================================================================

def machine_learning(df):
    """
    Perform machine learning tasks on the preprocessed dataset.
    """
    print("\n" + "="*50)
    print("MACHINE LEARNING")
    print("="*50)
    
    # 1. Prepare Data for Machine Learning
    print("\n1. Preparing Data for Machine Learning:")
    
    # Separate features and targets
    X = df.drop(['salary', 'job_satisfaction'], axis=1)
    y_salary = df['salary']
    y_satisfaction = df['job_satisfaction']
    
    # Split data into training and testing sets
    X_train, X_test, y_salary_train, y_salary_test = train_test_split(X, y_salary, test_size=0.2, random_state=42)
    _, _, y_satisfaction_train, y_satisfaction_test = train_test_split(X, y_satisfaction, test_size=0.2, random_state=42)
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")
    
    # 2. Regression: Salary Prediction
    print("\n2. Regression: Salary Prediction:")
    
    # Train a linear regression model
    reg_model = LinearRegression()
    reg_model.fit(X_train, y_salary_train)
    
    # Make predictions
    y_salary_pred = reg_model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_salary_test, y_salary_pred)
    rmse = np.sqrt(mse)
    r2 = reg_model.score(X_test, y_salary_test)
    
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Root Mean Squared Error: {rmse:.2f}")
    print(f"R-squared: {r2:.4f}")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': np.abs(reg_model.coef_)
    })
    feature_importance = feature_importance.sort_values('Importance', ascending=False)
    print("\nTop 10 most important features for salary prediction:")
    print(feature_importance.head(10))
    
    # 3. Classification: Job Satisfaction Prediction
    print("\n3. Classification: Job Satisfaction Prediction:")
    
    # Train a logistic regression model
    clf_model = LogisticRegression(max_iter=1000, random_state=42)
    clf_model.fit(X_train, y_satisfaction_train)
    
    # Make predictions
    y_satisfaction_pred = clf_model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_satisfaction_test, y_satisfaction_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_satisfaction_test, y_satisfaction_pred))
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': np.abs(clf_model.coef_[0])
    })
    feature_importance = feature_importance.sort_values('Importance', ascending=False)
    print("\nTop 10 most important features for job satisfaction prediction:")
    print(feature_importance.head(10))
    
    # 4. Visualization of Results
    print("\n4. Visualization of Results:")
    
    # Actual vs Predicted Salary
    plt.figure(figsize=(10, 6))
    plt.scatter(y_salary_test, y_salary_pred, alpha=0.5)
    plt.plot([y_salary_test.min(), y_salary_test.max()], [y_salary_test.min(), y_salary_test.max()], 'r--')
    plt.xlabel('Actual Salary')
    plt.ylabel('Predicted Salary')
    plt.title('Actual vs Predicted Salary')
    plt.tight_layout()
    plt.savefig('actual_vs_predicted_salary.png')
    print("Actual vs Predicted Salary plot saved as 'actual_vs_predicted_salary.png'")
    
    # Feature Importance for Salary Prediction
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Importance', y='Feature', data=feature_importance.head(10))
    plt.title('Top 10 Features for Salary Prediction')
    plt.tight_layout()
    plt.savefig('salary_feature_importance.png')
    print("Salary Feature Importance plot saved as 'salary_feature_importance.png'")
    
    return "Machine learning tasks completed successfully!"

# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main():
    print("ADVANCED DATA ANALYSIS WITH PANDAS AND NUMPY")
    print("===========================================")
    
    # Generate sample data
    df = generate_sample_data(n_samples=1000)
    
    # Perform exploratory data analysis
    eda_result = exploratory_data_analysis(df)
    print(eda_result)
    
    # Preprocess data
    df_processed = preprocess_data(df)
    
    # Perform machine learning tasks
    ml_result = machine_learning(df_processed)
    print(ml_result)
    
    print("\nAdvanced data analysis completed! Check the generated files for visualizations.")

if __name__ == "__main__":
    main() 