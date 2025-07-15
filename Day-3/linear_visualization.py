'''
When the value of variable increases or decreases with the increase or decrease in the value of another variable, 
then it is nothing but a linear relationship. When we visualize a linear relationship, it shows whether the
relationship between the two features is linear or not.
In this code, we will visualize the linear relationship between two variables using a scatter plot.
'''

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Instagram.csv", encoding = 'latin1')
data = data.dropna()
print(data.head())

print(data.columns)  # Check column names
print(data[["Impressions", "Likes"]].dtypes)  # Check data types
print(data.shape)  # Check if DataFrame is empty
print(data.head())  # Preview data


# Visualizing the relationship between Likes and Impressions
sns.set(style="whitegrid")
figure = px.scatter(data_frame = data, 
                    x="Impressions",
                    y="Likes", 
                    size="Likes", 
                    trendline="ols", 
                    title = "Relationship Between Likes and Impressions")
figure.show()

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Bewtween Likes & Impressions")
sns.regplot(x="Impressions", y="Likes", data=data)
plt.show()