import requests
import json
import os
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api = "7689323d700343f0a08540b691b2ffda"
account_sid = 'AC7c444605ac8430800b6d25ab3bc6e339'
auth_token = 'fd937233eb14eee4e4d60027a3cf4663'
client = Client(account_sid, auth_token)

response = requests.get(url=f"https://newsapi.org/v2/everything?q=tesla&apiKey={news_api}")
response.raise_for_status()
data = response.json()
first_3_articles = data["articles"][:3]
tesla_stock_api = "CAW41ZWIZ7RIG9S0"
api_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "TSLA",
    "interval": "60min",
    "apikey": "CAW41ZWIZ7RIG9S0"

}
response_to_tesla = requests.get(url= "https://www.alphavantage.co/query", params=api_parameters)
response_to_tesla.raise_for_status()
tesla_data = response_to_tesla.json()
closing_price_yesterday = float(tesla_data["Time Series (60min)"]["2022-08-12 20:00:00"]["4. close"])
closing_price_day_before_yesterday = float(tesla_data["Time Series (60min)"]["2022-08-11 20:00:00"]["4. close"])
difference = closing_price_yesterday - closing_price_day_before_yesterday
if difference > 0:
    up_down = "↗"
else:
    up_down = "↘"
percent = (difference/closing_price_yesterday) * 100
if abs(percent) >= 4:
    for article in first_3_articles:
        description = article["description"]
        title = article["title"]
        message = client.messages \
            .create(
            body=f"{COMPANY_NAME}: {up_down}{abs(percent)}%\nHeadline:{title}\nBrief:{description}",
            from_='+12532432332',
            to='+359893444257'
        )

        print(message.sid)
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

