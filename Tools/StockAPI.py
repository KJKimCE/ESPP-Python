from Tools import config
import requests
from requests import HTTPError
import datetime


def getParameters():
    parameters = {
        "chartByDay": "true",
        "token": config.API_KEY
    }

    return parameters


def getStockPrice(symbol, date):
    iex_params = getParameters()

    delta = 1
    if date == datetime.date.today():
        delta = -1

    price = 0
    for i in range(5):
        dateString = str(date.year) + format(date.month, '02') + format(date.day, '02')
        response = requests.get(f"https://cloud.iexapis.com/stable/stock/{symbol}/chart/date/{dateString}",
                                params=iex_params)

        if response.status_code == 200:
            jsonResponse = response.json()
            if not jsonResponse:
                date += datetime.timedelta(days=delta)
                continue

            stockResponse = {}
            for pair in jsonResponse:
                for key, val in pair.items():
                    stockResponse[key] = val

            price = float(stockResponse['uOpen'])
            break
        else:
            raise SystemExit(HTTPError(f"HTTP Status Code {response.status_code} returned for symbol: {symbol} on {date}"))

    if date > datetime.date.today():
        date = datetime.date.today()

    return price, date
