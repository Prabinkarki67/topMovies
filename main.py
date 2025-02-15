import urllib3
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?title_type=feature'
http = urllib3.PoolManager()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = http.request('GET', url, headers=headers)

if response.status == 200:
    soup = BeautifulSoup(response.data, 'html.parser')

    # Extract the text from the h1 tag with class ipc-title__text
    titles = soup.select("h3.ipc-title__text")  # Using CSS selectors)
    i=0
    for i in titles:
        print(i.text.strip())

