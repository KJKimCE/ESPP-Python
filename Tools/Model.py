import datetime
from dateutil.relativedelta import relativedelta
from Tools import Utils, StockAPI


class Model:
    grantDate = None
    exerciseDate = None
    purchaseDate = None
    today = None

    grantPrice = None
    exercisePrice = None
    purchasePrice = None
    discountedPrice = None
    quantity = None
    currentPrice = None

    transactionCost = None
    diversificationBenefit = None

    def __init__(self, symbol, quantity, purchaseDate, transactionCost, db):
        self.grantDate = purchaseDate + relativedelta(months=-2, day=1)
        self.purchaseDate = purchaseDate
        self.exerciseDate = purchaseDate
        self.today = datetime.date.today()

        self.grantPrice, self.grantDate = StockAPI.getStockPrice(symbol, self.grantDate)
        self.exercisePrice, self.exerciseDate = StockAPI.getStockPrice(symbol, self.exerciseDate)
        self.currentPrice, self.today = StockAPI.getStockPrice(symbol, self.today)
        self.purchasePrice = min(self.grantPrice, self.exercisePrice)
        self.discountedPrice = self.purchasePrice * (1 - 0.15)
        self.quantity = quantity

        self.transactionCost = transactionCost
        self.diversificationBenefit = db

    def print(self):
        print("Model:")
        print("Today: " + str(self.today))
        print("Current Price: " + Utils.formatCurrency(self.currentPrice))
        print("Grant Date: " + str(self.grantDate))
        print("Grant Price: " + Utils.formatCurrency(self.grantPrice))
        print("Exercise Date: " + str(self.exerciseDate))
        print("Exercise Price: " + Utils.formatCurrency(self.exercisePrice))
        print("Purchase Date: " + str(self.purchaseDate))
        print("Purchase Price: " + Utils.formatCurrency(self.purchasePrice))
        print("Discounted Price: " + Utils.formatCurrency(self.discountedPrice))
        print("Quantity: " + str(self.quantity))
        print("Transaction Cost: " + str(self.transactionCost))
        print("Diversification Benefit: " + str(self.diversificationBenefit * 100) + "%")
        print()
