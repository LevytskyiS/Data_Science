import requests
import pandas as pd
import numpy as np


url = "https://uk.wikipedia.org/wiki/Народжуваність_в_Україні"

page_html = requests.get(url=url).text
tabs = pd.read_html(page_html, header=0)
df = tabs[-12]

# Task 1.1
df.head(3)

# Task 1.2
df_shape = df.shape

# Task 1.4
df_dtypes = df.dtypes

# Task 1.6
columns = df.columns
total_missing_data = np.sum(pd.isnull(df[columns[1:]]))

# Task 1.7
df = df.drop([27])

# Task 1.8 Замініть відсутні дані в стовпцях середніми значеннями цих стовпців (метод fillna)
values = {
    "1950": df["1950"].mean(),
    "1960": df["1960"].mean(),
    "1970": df["1970"].mean(),
    "2014": df["2014"].mean(),
}
df = df.fillna(value=values)

# Task 1.9 Отримайте список регіонів, де рівень народжуваності у 2019 році був вищим за середній по Україні
y_2014_mean = df["2014"].mean()
result = df[df["2014"] > y_2014_mean][["регіон", "2014"]]

# Task 1.10 У якому регіоні була найвища народжуваність у 2014 році?
max_2014 = df["2014"].max()
max_2014_region = df[df["2014"] == max_2014][["регіон"]]

# Task 1.11 Побудуйте стовпчикову діаграму народжуваності по регіонах у 2019 році
