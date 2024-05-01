import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv('C:/Users/abc/Desktop/rm-cw2/Results_21Mar2022.csv')  # put dataset file path

# Remove the 'n_participants' column
if 'n_participants' in data.columns:
    data = data.drop(columns=['n_participants'])

# Generate a correlation matrix for numerical data
data_numeric = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = data_numeric.corr()

# Plot the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix for Numerical Data without \'n_participants\'')
plt.show()

