from bs4 import BeautifulSoup
import requests
data = requests.get("https://news.ycombinator.com/news")
# print(data.text)
yc_webpage = data.text
soup=BeautifulSoup(yc_webpage, "html.parser")
#get the html text of website and create a new html.txt
with open(file="news.html",mode="w") as f:
    f.write(soup.prettify())
# print(soup.prettify())
print(soup.title)
#find all names of news title
article_name= soup.find(name="span",class_="titleline").getText()
print(article_name)
article_link = soup.find(name="a")
print(article_link)
article = soup.find("tr", class_="athing")

title = article.find("span", class_="titleline").find("a")
title_link = title["href"]
score = article.find("span",class_="score")
print(score.text)

# website = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# html_web = website.text
subtext_row = article.find_next_sibling('tr')

# soup = BeautifulSoup(html_web,"lxml")
# print(soup)
# print(soup.title)