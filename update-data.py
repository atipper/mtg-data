# https://mtgjson.com/downloads/all-files/

from bs4 import BeautifulSoup
import requests

url = 'https://mtgjson.com/downloads/all-files/'
path = r'C:\Users\Andrew Tipper\Documents\Development\mtg-data\AllPrintings.json.zip'
response = requests.get(url)

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
print("Total Links Found:", links.__len__())

for link in links:
    href = link.get('href')
    if (href.find('AllPrintings.json.zip') > 1):
        download_url(href, path)
        print('Download of archive completed - ' + href)
