from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = ''
table_id = ''

response = requests.get(wiki_url)
soup = BeautifulSoup(response.test, 'html.parser')

x_table = soup.find('table', attr={'id': table_id})
df = pd.read_html(str(x_table))