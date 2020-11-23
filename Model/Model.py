from View.ModelParams import ModelParams
from Model import StockAPI
from Tools import Utils
import datetime
from dateutil.relativedelta import relativedelta


class Model:
    symbol = None
    quantity = None

    today = None
    currentPrice = None
    purchaseDate = None
    purchasePrice = None
    grantDate = None
    grantPrice = None
    exerciseDate = None
    exercisePrice = None
    discountedPrice = None

    transactionCost = None
    diversificationBenefit = None

    def __init__(self, modelParams: ModelParams):
        if not modelParams.valid:
            modelParams.validate()

        self.symbol = modelParams.symbol
        self.grantDate = modelParams.purchaseDate + relativedelta(months=-2, day=1)
        self.purchaseDate = modelParams.purchaseDate
        self.exerciseDate = modelParams.purchaseDate
        self.today = datetime.date.today()

        self.currentPrice, self.today = StockAPI.getStockPrice(modelParams.symbol, self.today)
        self.exercisePrice, self.exerciseDate = StockAPI.getStockPrice(modelParams.symbol, self.exerciseDate)
        self.grantPrice, self.grantDate = StockAPI.getStockPrice(modelParams.symbol, self.grantDate)
        self.purchasePrice = min(self.grantPrice, self.exercisePrice)
        self.discountedPrice = round(self.purchasePrice * (1 - 0.15), 2)
        self.quantity = modelParams.quantity

        self.transactionCost = modelParams.transactionCost
        self.diversificationBenefit = modelParams.db

    def print(self):
        print("Model:")
        print("Symbol: " + self.symbol)
        print("Quantity: " + str(self.quantity))
        print("Today: " + str(self.today))
        print("Current Price: " + Utils.formatCurrency(self.currentPrice))
        print("Purchase Date: " + str(self.purchaseDate))
        print("Purchase Price: " + Utils.formatCurrency(self.purchasePrice))
        print("Grant Date: " + str(self.grantDate))
        print("Grant Price: " + Utils.formatCurrency(self.grantPrice))
        print("Exercise Date: " + str(self.exerciseDate))
        print("Exercise Price: " + Utils.formatCurrency(self.exercisePrice))
        print("Discounted Price: " + Utils.formatCurrency(self.discountedPrice))
        print("Transaction Cost: " + str(self.transactionCost))
        print("Diversification Benefit: " + str(self.diversificationBenefit * 100) + "%")
        print()
