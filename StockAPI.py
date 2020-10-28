import requests
from requests import HTTPError
import datetime


def getStockPrice(symbol, date):
    iex_params = {
        "chartByDay": "true",
        "token": "pk_b2b9f0cda72d4f188877235a6ddf1146"
    }

    delta = 1
    if date == datetime.date.today():
        delta = -1

    for i in range(5):
        dateString = str(date.year) + format(date.month, '02') + format(date.day, '02')
        response = requests.get(f"https://cloud.iexapis.com/stable/stock/{symbol}/chart/date/{dateString}",
                                params=iex_params)

        price = 0
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
