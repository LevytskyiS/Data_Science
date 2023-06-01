import requests
import pandas as pd
import numpy as np
import seaborn as sns
from bs4 import BeautifulSoup
from unicodedata import normalize

url = "https://uk.wikipedia.org/wiki/Народжуваність_в_Україні"

page_html = requests.get(url=url).text
tabs = pd.read_html(page_html, header=0)
birth_rate_df = tabs[-12]
print(birth_rate_df.head(5))
