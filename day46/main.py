from bs4 import BeautifulSoup
import requests
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
url = "https://www.jiosaavn.com/featured/hindi-india-superhits-top-50/zlJfJYVuyjpxWb5,FqsjKg__"
response = requests.get(url=url, headers=header)
response.raise_for_status()
song_data=response.text
# print(song_data)
soup = BeautifulSoup(song_data,"html.parser")
with open(file="songs.html",mode="w",encoding="utf-8") as f:
    f.write(soup.prettify())
print(soup.title)
songs = soup.select("div.o-flag__body div a")
for song in songs:
    print(song.get_text(strip=True))
