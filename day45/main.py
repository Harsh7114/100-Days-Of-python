from bs4 import BeautifulSoup
# import lxml
with open (file="website.html",mode="r") as f:
    data = f.read()
soup = BeautifulSoup(data,"html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())

all_anchor_tag=soup.find_all(name="a")
print(all_anchor_tag)

for tag in all_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))
heading = soup.find(name="h1",id="name")
section_heading = soup.find(name="h3",class_="heading")

company_url = soup.select_one(selector="p a")
print(company_url)
