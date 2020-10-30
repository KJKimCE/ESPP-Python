from Tools.Model import Model
from Tools.TaxBracket import TaxBracket
from Tools.Regime import CurrentSales
from Tools.FutureSale import FutureSale
from Tools import config
import datetime


def checkAPIKey():
    if config.API_KEY == "YOUR_API_KEY_HERE":
        raise SystemExit(Exception("Please replace the API Key. Instructions are detailed in the README"))


def getModel():
    symbol = input("Enter the stock symbol: ")
    quantity = int(input("Enter the quantity: "))
    purchaseDate = None
    while True:
        date = input("Enter the purchase date (yyyymmdd): ")
        try:
            purchaseDate = datetime.datetime.strptime(date, "%Y%m%d").date()
        except ValueError:
            print(f"Invalid date: {date}.")
            print()
            continue
        if purchaseDate > datetime.date.today():
            print(f"Future date cannot be earlier than {datetime.date.today()}.")
            print()
            continue
        break

    transactionCost = float(input("Enter the transaction cost: "))
    db = float(input("Enter the diversification benefit % (xx.xx): "))

    model = Model(symbol, quantity, purchaseDate, transactionCost, db / 100)
    return model


def getTaxBracket():
    income = float(input("Enter Tax Bracket % (xx.xx) - Income: "))
    shortTerm = float(input("Enter Tax Bracket % (xx.xx) - Short Term: "))
    longTerm = float(input("Enter Tax Bracket % (xx.xx) - Long Term: "))

    taxBracket = TaxBracket(income / 100, shortTerm / 100, longTerm / 100)

    return taxBracket


def runESPP():
    checkAPIKey()
    model = getModel()
    taxBracket = getTaxBracket()

    model.print()
    taxBracket.print()
    print('****************************************************')

    cs = CurrentSales(model, taxBracket)
    cs.print()

    while True:
        print('****************************************************')
        print("*Note: Enter 0 to exit")
        date = input("Enter the future date (yyyymmdd): ")
        if date == '0':
            break

        try:
            futureDate = datetime.datetime.strptime(date, "%Y%m%d").date()
        except ValueError:
            print(f"Invalid date: {date}.")
            print()
            continue

        if futureDate < datetime.date.today():
            print(f"Future date cannot be earlier than {datetime.date.today()}.")
            print()
            continue

        future = FutureSale(model, taxBracket, cs, futureDate)
        future.print()


if __name__ == '__main__':
    runESPP()
