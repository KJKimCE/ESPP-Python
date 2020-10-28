import Utils


class Benefit:
    regimeType = None
    diversificationBenefit = None
    pastProceeds = None
    finalProceeds = None
    difference = None

    def __init__(self, model, taxBracket, regime, future):
        self.regimeType = regime.regimeType
        self.diversificationBenefit = regime.finalProceeds * model.diversificationBenefit * ((future.date - max(regime.dateFrom, model.today)).days / 365.0)
        self.pastProceeds = regime.finalProceeds + self.diversificationBenefit
        self.finalProceeds = self.pastProceeds * (1 + future.expectedReturn * (1 - taxBracket.longTerm))
        self.difference = future.regime.finalProceeds - self.finalProceeds

    def print(self):
        print(f"Diversification Benefit - {self.regimeType}")
        print(f"Diversification Benefit: {Utils.formatCurrency(self.diversificationBenefit)}")
        print(f"Past Proceeds: {Utils.formatCurrency(self.pastProceeds)}")
        print(f"Final Proceeds: {Utils.formatCurrency(self.finalProceeds)}")
        print(f"Difference: {Utils.formatCurrency(self.difference)}")
        print()
