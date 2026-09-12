import os
import json
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import  requests
from dotenv import load_dotenv
load_dotenv()
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
data = requests.get(url="https://www.alphavantage.co/query",params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":os.getenv("STOCK_DATA")
})
data.raise_for_status()
stock_data = data.json()
with open("data.json", "w") as f:
    json.dump(stock_data, f, indent=4)
daily_data = stock_data["Time Series (Daily)"]
dates = list(daily_data.keys())
latest_date = dates[0]
previous_date = dates[1]
latest_close_stock = float(daily_data[latest_date]["4. close"])
previous_close_stock = float(daily_data[previous_date]["4. close"])
difference = latest_close_stock-previous_close_stock
#percentage cgange
percentage_change = ((latest_close_stock - previous_close_stock) / previous_close_stock) * 100
print(percentage_change)
up_down = None
if difference > 0:
    up_down = "+"
else:
    up_down = "-"
#if abs(percentage_change) >= 5:
if True:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_data = requests.get(
        url="https://newsapi.org/v2/everything",
        params={
            "apiKey": os.getenv("NEWS_API"),
            "qInTitle": "Tesla",
            "pageSize": 3,
            "sortBy": "relevancy",
            "language": "en"
        }
    )
    news_data.raise_for_status()
    news_related_to_stock=news_data.json()
    with open(file="news.json",mode="w") as f:
        json.dump(news_related_to_stock,f,indent=4)
    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's
    # title and description to your phone number.

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    for article in news_related_to_stock["articles"]:
        formatted_article = (
            f"{STOCK}: {up_down}{abs(percentage_change):.1f}%\n"
            f"{article['title'][:50]}\n"
            f"{article['description'][:50]}"
        )
        print("MESSAGE:")
        print(formatted_article)
        print("LENGTH:", len(formatted_article))
        print("----------------")

        message = client.messages.create(
            body=formatted_article,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("MY_PHONE_NUMBER")
        )
 
        print(message.status)



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

