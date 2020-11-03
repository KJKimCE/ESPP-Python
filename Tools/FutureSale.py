from Tools.Regime import DisqualifyingShort
from Tools.Regime import DisqualifyingLong
from Tools.Regime import Qualifying
from Tools.Benefit import Benefit
from Tools import Utils
import heapq


class FutureSale:
    regime = None
    date = None
    expectedReturn = None
    predictedPrice = None
    benefits = None
    regimes = None

    def __init__(self, model, taxBracket, currentSales, futureDate):
        self.benefits = []
        self.regimes = []
        self.date = futureDate
        self.expectedReturn = abs(self.date - model.today).days / 365.0 * .08
        self.predictedPrice = model.currentPrice * (1 + self.expectedReturn)

        benefitIndex = 0
        for regime in currentSales:
            if regime.dateFrom <= self.date < regime.dateTo:
                if regime.regimeType == 'Disqualifying Short':
                    self.regime = DisqualifyingShort(model, taxBracket, self.predictedPrice)
                    break
                elif regime.regimeType == 'Disqualifying Long':
                    self.regime = DisqualifyingLong(model, taxBracket, self.predictedPrice)
                    break
                elif regime.regimeType == 'Qualifying':
                    self.regime = Qualifying(model, taxBracket, self.predictedPrice)
                    break
            benefitIndex += 1

        heapq.heappush(self.regimes, (-1 * self.regime.finalProceeds, self.regime.regimeType))
        benefitIndex -= 1
        while benefitIndex >= 0:
            benefit = Benefit(model, taxBracket, currentSales[benefitIndex], self)
            self.benefits.append(benefit)

            heapq.heappush(self.regimes, (-1 * benefit.finalProceeds, benefit.regimeType))
            # self.regimes.append((benefit.difference, benefit.regimeType))
            benefitIndex -= 1

    def print(self):
        print(f"Future - {self.regime.regimeType}")
        print(f"Date: {self.date}")
        print(f"Expected Return: {'{:,.2f}'.format(self.expectedReturn * 100) + '%'}")
        print(f"Predicted Price: {Utils.formatCurrency(self.predictedPrice)}")
        print(f"Proceeds: {Utils.formatCurrency(self.regime.saleProceeds)}")
        print(f"Profit: {Utils.formatCurrency(self.regime.saleProfit)}")
        print(f"Income: {Utils.formatCurrency(self.regime.income)}")
        print(f"Short Term: {Utils.formatCurrency(self.regime.shortTerm)}")
        print(f"Long Term: {Utils.formatCurrency(self.regime.longTerm)}")
        print(f"Tax: {Utils.formatCurrency(self.regime.tax)}")
        print(f"Final Proceeds: {Utils.formatCurrency(self.regime.finalProceeds)}")
        print()

        for benefit in self.benefits:
            benefit.print()

        print(f"DECISION: {heapq.heappop(self.regimes)[1]}")
        print()
