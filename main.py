from Model.Model import Model
from Model.TaxBracket import TaxBracket
from Model.Regime import DisqualifyingShort, DisqualifyingLong, Qualifying
from Model.FutureSale import FutureSale
from Tools import config
from View.ModelParams import ModelParams
from View.TaxBracketParams import TaxBracketParams
import datetime


def checkAPIKey():
    if config.API_KEY == "YOUR_API_KEY_HERE":
        raise SystemExit(Exception("Please replace the API Key. Instructions are detailed in the README"))


def getModel():
    modelParams = ModelParams()
    modelParams.symbol = input("Enter the stock symbol: ")
    modelParams.quantity = int(input("Enter the quantity: "))

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
    modelParams.purchaseDate = date
    modelParams.transactionCost = float(input("Enter the transaction cost: "))
    modelParams.db = float(input("Enter the diversification benefit % (xx.xx): "))
    if not modelParams.valid:
        modelParams.validate()

    return Model(modelParams)


def getTaxBracket():
    taxBracketParams = TaxBracketParams()
    taxBracketParams.income = float(input("Enter Tax Bracket % (xx.xx) - Income: "))
    taxBracketParams.shortTerm = float(input("Enter Tax Bracket % (xx.xx) - Short Term: "))
    taxBracketParams.longTerm = float(input("Enter Tax Bracket % (xx.xx) - Long Term: "))

    if not taxBracketParams.valid:
        taxBracketParams.validate()

    return TaxBracket(taxBracketParams)


def getCurrentSales(model, taxBracket):
    regimes = [DisqualifyingShort(model, taxBracket, model.currentPrice),
               DisqualifyingLong(model, taxBracket, model.currentPrice),
               Qualifying(model, taxBracket, model.currentPrice)]

    return regimes


def printLine():
    print('****************************************************')


def runFutureSaleModel(model, taxBracket, currentSales):
    while True:
        printLine()
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

        future = FutureSale(model, taxBracket, currentSales, futureDate)
        future.print()


def runESPP():
    checkAPIKey()
    model = getModel()
    taxBracket = getTaxBracket()

    model.print()
    taxBracket.print()

    currentSales = getCurrentSales(model, taxBracket)
    for regime in currentSales:
        regime.print()

    runFutureSaleModel(model, taxBracket, currentSales)


if __name__ == '__main__':
    runESPP()
