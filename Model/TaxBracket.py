from View.TaxBracketParams import TaxBracketParams


class TaxBracket:
    income = None
    shortTerm = None
    longTerm = None

    def __init__(self, taxBracketParams: TaxBracketParams):
        if not taxBracketParams.valid:
            taxBracketParams.validate()

        self.income = taxBracketParams.income
        self.shortTerm = taxBracketParams.shortTerm
        self.longTerm = taxBracketParams.longTerm

    def print(self):
        print("Tax Brackets:")
        print(f"Income: {self.income * 100}%")
        print(f"Short Term: {self.shortTerm * 100}%")
        print(f"Long Term: {self.longTerm * 100}%")
        print()
