from bs4 import BeautifulSoup
from pathlib import  Path
import os
import requests
import smtplib
from dotenv import load_dotenv
Base_DIR  = Path(__file__).parent
load_dotenv(Base_DIR/".env")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
url = "https://www.amazon.in/Motorola-Edge-Lily-256GB-Storage/dp/B0G75Q7TDP/ref=sr_1_1?crid=1OIY64ZT3LU66&dib=eyJ2IjoiMSJ9.gHcdj1kkQb7B_RgqmvmErFBeZEMBVubDnBMlGDTkrtN7cfv8sTp857W-wOycCqgJntqPevGqR9OtpXhvPsE4WM26qo4q_ZNItuFLXgFLL2_XsL6mJOBGSAJVtUIlTiCALA4sf4QqWquGBwuRbGgZQ-bobWHvEOJaZQ0gCPEAlVZXmUUAN0khXsdQir_TUqkNo4UyWo9QuNyKYnBovcGpfFj9EmdT7wOGfz4umo8w3mo.g178mKG0_Da_bJLsNDkzYCzonSmNOFxZGhjWg5pl1xs&dib_tag=se&keywords=phone+moto+edge+70&qid=1794064127&sprefix=phone+moto+%2Caps%2C278&sr=8-1"
response = requests.get(url=url,headers=header)
response.raise_for_status()
website_data = response.text
soup = BeautifulSoup(website_data,"html.parser")
with open(file="website.html",mode="w",encoding="utf-8") as f:
    f.write(soup.prettify())
price = soup.select_one("div.a-section.apex-core-price-identifier div span")

if price:
    current_price = price.get_text(strip=True)
    print(current_price)
    # need to convert price fromn str to int
    current_price=current_price.replace("₹","").replace(",","")
    current_price=float(current_price)
    print(type(current_price))
    if(current_price<=40000):
        print("best time to purchase the product")
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=os.getenv("EMAIL_ADDRESS"),password=os.getenv("EMAIL_PASSWORD"))
            connection.sendmail(from_addr = os.getenv("EMAIL_ADDRESS"),
                                to_addrs="ranjanharsh236@gmail.com",
                                msg=f"Subject: Amazon Price Alert!\n\nbest time to purchase Motorola Edge 70 (Lily Pad, 8GB RAM, 256GB Storage)\n current price is {current_price}"
                                )
else:
    print("Price element not found")

