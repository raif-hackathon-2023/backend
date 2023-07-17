import requests
from bs4 import BeautifulSoup

with open('output.txt', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
    text = soup.get_text()

with open('input.txt', 'w') as f:
    f.write(text)