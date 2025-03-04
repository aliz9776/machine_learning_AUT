# -*- coding: utf-8 -*-
"""HW2-ML-Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jwOb3BZsumVMbSLaFe7IBA7Mr58eQy6T

Problem 2: Cancer | Preprocessing Dataset

Cancer is a major health concern worldwide, and it is one of the leading causes of death globally. According to the World Health Organization (WHO), cancer is responsible for an estimated 9.6 million deaths worldwide in 2018, making it the second leading cause of death after cardiovascular diseases. The cancer dataset is a well-known dataset that is often used in machine learning research. It contains measurements of various features of breast mass samples that can be used to predict whether a mass is benign (non-cancerous) or malignant (cancerous). The dataset was originally compiled by Dr. William H. Wolberg. The dataset contains a total of 569 instances, with 212 instances corresponding to malignant masses and 357 instances corresponding to benign masses. cancer.csv has been provided in the exercise file, which is a collection of personal information and the likelihood of each person's cancer between 0 and 1. Some columns have been removed from this dataset for various reasons, and of course, many data are incomplete. In this exercise, we ask you to perform the following tasks on the dataset in the best possible way:

a) Load the data and convert the cancer probability from a number to an optimal 5-category. Explain how you do this.
"""

import pandas as pd

# Load the dataset with tab as delimiter
cancer_df = pd.read_csv('cancer.csv', delimiter='\t')

# Define bin edges and labels
bin_edges = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
bin_labels = ['Very Low', 'Low', 'Moderate', 'High', 'Very High']

# Use cut function to create 5-category variable
cancer_df['cancer_category'] = pd.cut(cancer_df['prob_cancer'], bins=bin_edges, labels=bin_labels)

# Display the updated dataset
print(cancer_df.head())

"""b) Describe the problems with the height column data and try to implement the best solution for it and apply it to the data."""

# Convert 'height' column to numeric format, and replace invalid values with NaN
cancer_df['height'] = pd.to_numeric(cancer_df['height'], errors='coerce')

# Replace missing values in 'height' column with mean value
mean_height = cancer_df['height'].mean()
cancer_df['height'].fillna(mean_height, inplace=True)

# Convert 'height' column to centimeters (assuming it's in inches)
cancer_df['height_cm'] = cancer_df['height'] * 2.54

# Display the updated dataset
print(cancer_df.head())

"""c) Remove the rows that have empty or invalid data in the current_smoking column"""

# Drop rows with missing values in 'current_smoking' column
cancer_df.dropna(subset=['current_smoking'], inplace=True)

# Display the updated dataset
print(cancer_df.head())

"""d) Fill the remaining empty or invalid data in other columns with the mean of all data."""

# Calculate the mean of all non-null values in the dataframe
mean_values = cancer_df.mean()

# Fill empty or invalid data in other columns with the mean values
cancer_df.fillna(mean_values, inplace=True)

# Display the updated dataset
print(cancer_df.head())

"""e) Remove additional columns.


"""

# List of additional columns to be removed
additional_columns = ['weight', 'salads_per_week', 'veggies_fruits_per_day' , 'user_id', 'prob_cancer']

# Drop the additional columns from the dataframe
cancer_df.drop(columns=additional_columns, inplace=True)

# Display the updated dataset
print(cancer_df.head())

"""f) Divide the data into two parts of training and testing (70/30) and standardize the data."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , OneHotEncoder, LabelEncoder


# Label encode current_smoking column
le = LabelEncoder()
cancer_df['current_smoking'] = le.fit_transform(cancer_df['current_smoking'])

# One-hot encode categorical columns
categorical_cols = ['healthy_diet', 'cancer_category']
encoder = OneHotEncoder()
cancer_df_encoded = pd.get_dummies(cancer_df, columns=categorical_cols)

# Divide the data into training and testing sets (70/30 split)
X = cancer_df_encoded.drop(columns=['cancer_category_Very High'])  # Exclude one category as reference
y = cancer_df_encoded['cancer_category_Very High']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""g) Train the data using the knn algorithm with k=5 and classify it."""

from sklearn.neighbors import KNeighborsClassifier


# Create KNN classifier with k=5
knn = KNeighborsClassifier(n_neighbors=5)

# Train the model on the scaled training data
knn.fit(X_train_scaled, y_train)

# Make predictions on the scaled testing data
y_pred = knn.predict(X_test_scaled)

"""h) Obtain the Confusion matrix, R2_Score, and Accuracy."""

from sklearn.metrics import confusion_matrix, r2_score, accuracy_score

# Obtain confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Calculate R2 score
r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""i) Try another Preprocessing methods to improve results."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, r2_score

# Load the data
df = pd.read_csv('cancer.csv' , delimiter='\t' )

# Convert cancer probability to 5 categories
df['cancer_category'] = pd.cut(df['prob_cancer'], bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
                               labels=['very low', 'low', 'medium', 'high', 'very high'])

# Drop irrelevant columns
df = df.drop(columns=['user_id', 'survey.month', 'prob_cancer'])

# Fill missing values with the mean
df = df.fillna(df.mean())

# Drop rows with missing or invalid data in current_smoking column
df = df.dropna(subset=['current_smoking'])

# Convert height to centimeters
df['height'] = np.where(df['height'] > 100, df['height'], df['height']*100)

# One-hot encode categorical columns
categorical_cols = ['healthy_diet']
encoder = OneHotEncoder()
# fit and transform the data
X_encoded = encoder.fit_transform(X)

# get the feature names after one-hot encoding
onehot_cols = encoder.get_feature_names_out(X.columns)

df = pd.concat([df, onehot_cols], axis=1)
df = df.drop(columns=categorical_cols)

# Split data into train and test sets
X = df.drop(columns=['cancer_category'])
y = df['cancer_category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
numerical_cols = ['weight', 'height', 'salads_per_week', 'veggies_fruits_per_day',
                  'aerobic_per_week', 'sports_per_week']
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

# Train the KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict the test set
y_pred = knn.predict(X_test)

# Evaluate the model
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
r2 = r2_score(y_test, y_pred, multioutput='variance_weighted')

print('Confusion Matrix:')
print(cm)
print('Accuracy:', acc)
print('R2 Score:', r2)