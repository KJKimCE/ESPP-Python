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
        self.quantity = Utils.formatInt(self.quantity, "Quantity")
        self.purchaseDate = Utils.formatDate(self.purchaseDate)
        if self.purchaseDate > Utils.runDate:
            raise ValueError(f"Invalid Purchase Date: {self.purchaseDate}")
        self.transactionCost = Utils.formatFloat(self.transactionCost, "Transaction Cost")
        self.db = Utils.formatFloat(self.db, "Diversification Benefit") / 100
