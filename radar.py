import pandas as pd
import numpy as np
import plotly.graph_objects as go  
from sklearn.preprocessing import MinMaxScaler



# read CSV data
path_to_csv = 'C:/Users/abc/Desktop/rm-cw2/Results_21Mar2022.csv'
df = pd.read_csv(path_to_csv)

# normalize
columns_to_normalize = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 
    'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid'
]

# normalize
scaler = MinMaxScaler()
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# remove outlier
Q1 = df[columns_to_normalize].quantile(0.25)
Q3 = df[columns_to_normalize].quantile(0.75)
IQR = Q3 - Q1
df_cleaned = df[~((df[columns_to_normalize] < (Q1 - 1.5 * IQR)) | (df[columns_to_normalize] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Initialize empty image
fig = go.Figure()

#Traverse unique 'grouping' values
for grouping_value in df_cleaned['grouping'].unique():
    df_group = df_cleaned[df_cleaned['grouping'] == grouping_value]
    radar_data = df_group[columns_to_normalize].mean().reset_index()
    radar_data.columns = ['Indicator', 'Value']
    theta = radar_data['Indicator'].tolist()
    
    # Add a layer of data on the radar map
    fig.add_trace(
        go.Scatterpolar(
            r=radar_data['Value'],
            theta=theta,
            fill='toself',
            name=grouping_value  
        )
    )

fig.update_layout(
  polar=dict(radialaxis=dict(visible=True)),
  showlegend=True
)

fig.show()

