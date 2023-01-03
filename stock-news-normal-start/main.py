import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

API_KEY = "KUWG880DOZ8C675X"


parameters = {
    "function" = "TIME_SERIES_DAILY";
    "symbol" = STOCK_NAME;
    "apikey" = API_KEY;
}
response = reuqest.get(STOCK_ENDPOINT, params = parameters)
data = response.json()["TIMES_SERIES_DAILY"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4, close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4, close"]
print(day_before_yesterday_data_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price)
print(difference)

diff_percent = (difference / float(yesterday_closing_price))*100

if diff_percent >5:
    print("Get News") 
    