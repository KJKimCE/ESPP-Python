from Model import Model
from TaxBracket import TaxBracket
from Regime import CurrentSales
from FutureSale import FutureSale
import datetime


def test():

    symbol = input("Enter the stock symbol: ")
    quantity = int(input("Enter the quantity: "))
    date = input("Enter the purchase date (yyyymmdd): ")
    transactionCost = float(input("Enter the transaction cost: "))
    db = float(input("Enter the diversification benefit % (xx.xx): "))
    purchaseDate = datetime.datetime.strptime(date, "%Y%m%d").date()
    income = float(input("Enter Tax Bracket % (xx.xx) - Income: "))
    shortTerm = float(input("Enter Tax Bracket % (xx.xx) - Short Term: "))
    longTerm = float(input("Enter Tax Bracket % (xx.xx) - Long Term: "))

    model = Model(symbol, quantity, purchaseDate, transactionCost, db / 100)
    model.print()

    taxBracket = TaxBracket(income / 100, shortTerm / 100, longTerm / 100)
    taxBracket.print()

    cs = CurrentSales(model, taxBracket)
    cs.print()

    date = input("Enter the future date (yyyymmdd): ")
    futureDate = datetime.datetime.strptime(date, "%Y%m%d").date()

    future = FutureSale(model, taxBracket, cs, futureDate)
    future.print()


if __name__ == '__main__':
    test()

