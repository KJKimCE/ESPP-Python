from View.MainView import MainView
from Model.Model import Model
from Model.TaxBracket import TaxBracket
from Model.Regime import DisqualifyingShort, DisqualifyingLong, Qualifying
from Model.FutureSale import FutureSale
from View.ModelParams import ModelParams
from View.ModelView import ModelView
from View.FutureView import FutureView
from Tools import Utils


def changed(model: Model, modelParams: ModelParams):
    return model.symbol == modelParams.symbol and model.purchaseDate == modelParams.purchaseDate


def getCurrentSales(model, taxBracket):
    regimes = [DisqualifyingShort(model, taxBracket, model.currentPrice),
               DisqualifyingLong(model, taxBracket, model.currentPrice),
               Qualifying(model, taxBracket, model.currentPrice)]

    return regimes


class Controller:
    main_view: MainView = None
    model: Model = None
    taxBracket: TaxBracket = None
    currentSales = None

    # region Initialize
    def __init__(self):
        self.main_view = MainView(self)
    # endregion

    # region Switch Frame (public)
    def showFrame(self, container):
        self.main_view.show_frame(container)
    # endregion

    # region Run Model (public)
    def runModel(self, model_view: ModelView):
        try:
            self._computeModel(model_view)
            self._computeTaxBracket(model_view)
        except ValueError as err:
            model_view.renderError(err)
            return

        model_view.renderModel()

        self.currentSales = getCurrentSales(self.model, self.taxBracket)
        model_view.renderCurrentSales(self.currentSales)
        model_view.renderFutureButton()

    # region Compute Model (private)

    def _computeModel(self, model_view: ModelView):
        modelParams = model_view.get_model_params()
        modelParams.validate()

        if self.model is None or self.model.symbol != modelParams.symbol or self.model.purchaseDate != modelParams.purchaseDate:
            self.model = Model(modelParams)
        else:
            # Stock symbol and purchase date are unchanged -- don't re-run the Stock Price API
            self.model.quantity = modelParams.quantity
            self.model.transactionCost = modelParams.transactionCost
            self.model.diversificationBenefit = modelParams.db

    def _computeTaxBracket(self, model_view: ModelView):
        taxBracketParams = model_view.get_tax_bracket_params()
        taxBracketParams.validate()

        self.taxBracket = TaxBracket(taxBracketParams)
    # endregion
    # endregion

    # region Run Future (public)
    def runFuture(self, future_view):
        try:
            future = self._computeFutureSale(future_view)
        except ValueError as err:
            future_view.renderError(err)
            return

        future_view.renderFutureSale(future)

    # region Compute Future (private)
    def _computeFutureSale(self, future_view: FutureView):
        futureDate = future_view.getFutureDate()
        futureDate = Utils.validateDate(futureDate)
        return FutureSale(self.model, self.taxBracket, self.currentSales, futureDate)
    # endregion
    # endregion

    # region Main Function
    def main(self):
        self.main_view.main()
    # endregion


if __name__ == '__main__':
    controller = Controller()
    controller.main()
