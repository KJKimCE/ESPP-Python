from Tools import Utils


class ModelParams:
    symbol = None
    quantity = None
    purchaseDate = None
    transactionCost = None
    db = None
    valid = False

    def validate(self):
        self.valid = True
        self.symbol = self.symbol.upper()
        self.quantity = int(self.quantity)
        self.purchaseDate = Utils.validateDate(self.purchaseDate)
        self.transactionCost = float(self.transactionCost)
        self.db = float(self.db) / 100
