def validateTaxBracket(bracket):
    try:
        return float(bracket) / 100
    except ValueError:
        raise ValueError(f"Invalid Tax Bracket: {bracket}.")


class TaxBracketParams:
    income = None
    shortTerm = None
    longTerm = None
    valid = False

    def validate(self):
        self.valid = True
        self.income = validateTaxBracket(self.income)
        self.shortTerm = validateTaxBracket(self.shortTerm)
        self.longTerm = validateTaxBracket(self.longTerm)
