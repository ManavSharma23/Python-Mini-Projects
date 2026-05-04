import requests

Stock_Name = "TSLA"
Company = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = "NDJF9L5AH6E175GS"

stock_parameter={
    "function": "TIME_SERIES_DAILY",
    "symbol": Stock_Name,
    "apikey": API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameter)
main_data=response.json()["Time Series (Daily)"]
data = [value for (key, value) in main_data.items()]
print("status : ",response.status_code)

yesterday=data[0]
yesterday_data=yesterday["4. close"]

day_before_yesterday=data[1]
day_before_yesterday_data=day_before_yesterday["4. close"]
print(yesterday_data)
print(day_before_yesterday_data)
