from Tools import Utils
from abc import ABCMeta, abstractmethod
import datetime


class Regime(metaclass=ABCMeta):
    regimeType = None
    saleProceeds = None
    saleProfit = None
    income = None
    shortTerm = None
    longTerm = None
    tax = None
    finalProceeds = None

    dateFrom = None
    dateTo = None

    def __init__(self, model, taxBracket, price):
        self.calculateSales(model, price)
        self.calculateRegime(model)
        self.calculateTaxes(taxBracket)

    def calculateSales(self, model, price):
        self.saleProceeds = model.quantity * price - model.transactionCost
        self.saleProfit = self.saleProceeds - model.quantity * model.discountedPrice

    @abstractmethod
    def calculateRegime(self, model):
        pass

    def calculateTaxes(self, taxBracket):
        self.tax = self.income * taxBracket.income + self.shortTerm * taxBracket.shortTerm + self.longTerm * taxBracket.longTerm
        self.finalProceeds = self.saleProceeds - self.tax

    def print(self):
        print(self.regimeType)
        print(f"Date From: {self.dateFrom}")
        print(f"Date To: {self.dateTo}")
        print(f"Sale Proceeds: {Utils.formatCurrency(self.saleProceeds)}")
        print(f"Sale Profit: {Utils.formatCurrency(self.saleProfit)}")
        print(f"Income: {Utils.formatCurrency(self.income)}")
        print(f"Short Term: {Utils.formatCurrency(self.shortTerm)}")
        print(f"Long Term: {Utils.formatCurrency(self.longTerm)}")
        print(f"Tax: {Utils.formatCurrency(self.tax)}")
        print(f"Final Proceeds: {Utils.formatCurrency(self.finalProceeds)}")
        print()


class DisqualifyingShort(Regime):
    def calculateRegime(self, model):
        self.regimeType = "Disqualifying Short"
        self.dateFrom = model.exerciseDate + datetime.timedelta(days=45)
        self.dateTo = model.purchaseDate + datetime.timedelta(days=365+45)

        self.income = model.quantity * (model.exercisePrice - model.discountedPrice)
        self.shortTerm = self.saleProfit - self.income
        self.longTerm = 0


class DisqualifyingLong(Regime):
    def calculateRegime(self, model):
        self.regimeType = "Disqualifying Long"
        self.dateFrom = model.purchaseDate + datetime.timedelta(days=365+45)
        self.dateTo = max(model.grantDate + datetime.timedelta(days=730), model.exerciseDate + datetime.timedelta(days=365+15))

        self.income = model.quantity * (model.exercisePrice - model.discountedPrice)
        self.shortTerm = 0
        self.longTerm = self.saleProfit - self.income


class Qualifying(Regime):
    def calculateRegime(self, model):
        self.regimeType = "Qualifying"
        self.dateFrom = max(model.grantDate + datetime.timedelta(days=730), model.exerciseDate + datetime.timedelta(days=365+15))
        self.dateTo = datetime.date.max

        self.income = model.quantity * max(min(model.currentPrice - model.discountedPrice - model.transactionCost, .15 * model.grantPrice), 0.0)
        self.shortTerm = 0
        self.longTerm = self.saleProfit - self.income
