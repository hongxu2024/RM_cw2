import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler


# path of CSV file
path_to_csv = 'C:/Users/abc/Desktop/rm-cw2/Results_21Mar2022.csv'

# Read data from CSV file
df = pd.read_csv(path_to_csv)




columns_to_normalize = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 
    'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid'
]

# Normalize specified columns
scaler = MinMaxScaler()
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# Logic for removing outliers
Q1 = df[columns_to_normalize].quantile(0.25)
Q3 = df[columns_to_normalize].quantile(0.75)
IQR = Q3 - Q1
df_cleaned = df[~((df[columns_to_normalize] < (Q1 - 1.5 * IQR)) | (df[columns_to_normalize] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Specify the names of the indicators you want to present in the box plot
scale_columns = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid']

# Convert the cleaned DataFrame into a long format for easier plotting
df_cleaned_long = df_cleaned.melt(id_vars=['grouping'], value_vars=scale_columns, var_name='Variable', value_name='Scaled_Value')

# Create box plot
# fig = px.box(df_cleaned_long, x='Variable', y='Scaled_Value', color='grouping', title='Normalized Environmental Impact Indicators - Cleaned')
fig = px.box(df_cleaned_long, x='Variable', y='Scaled_Value', color='grouping')

# Display the figure
fig.show()
