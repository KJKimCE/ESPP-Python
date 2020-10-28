class TaxBracket:
    income = None
    shortTerm = None
    longTerm = None

    def __init__(self, income, shortTerm, longTerm):
        self.income = income
        self.shortTerm = shortTerm
        self.longTerm = longTerm

    def print(self):
        print("Tax Brackets:")
        print(f"Income: {self.income * 100}%")
        print(f"Short Term: {self.shortTerm * 100}%")
        print(f"Long Term: {self.longTerm * 100}%")
        print()
