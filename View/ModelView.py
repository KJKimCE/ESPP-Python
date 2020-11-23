from View.ModelParams import ModelParams
from View.TaxBracketParams import TaxBracketParams
import View.FutureView as FutureView
from Tools import Utils
import tkinter as tk
from tkinter import ttk


PADGRID = 5
STICKYGRID = 'W'
SPAN = 2


class ModelView(tk.Frame):
    error_frame = None
    model_response_frame = None
    tax_response_frame = None
    regime_frame = None
    future_button = None

    # region Initialize
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self, parent_frame)
        self.controller = controller

        self._make_model_frames()
        self._make_tax_bracket_frames()
        self._make_button()
    # endregion

    # region Make Frames (private)
    def _make_model_frames(self):
        top_frame = tk.Frame(self)
        top_frame.pack()
        tk.Label(top_frame, text='Enter Model Information').pack()

        stock_frame = tk.Frame(self)
        stock_frame.pack()

        self.symbol = Utils.create_entry(stock_frame, 'Stock Symbol:')
        self.quantity = Utils.create_entry(stock_frame, 'Quantity:')
        self.purchase_date = Utils.create_entry(stock_frame, 'Purchase Date (yyyymmdd):')

        model_input_frame = tk.Frame(self)
        model_input_frame.pack()

        self.transaction_cost = Utils.create_entry(model_input_frame, 'Transaction Cost:')
        self.db = Utils.create_entry(model_input_frame, 'Diversification Benefit (%):')

    def _make_tax_bracket_frames(self):
        top_frame = tk.Frame(self)
        top_frame.pack(side='top')
        tk.Label(top_frame, text='Enter Tax Bracket Information (%)').pack()

        tax_bracket_input_frame = tk.Frame(self)
        tax_bracket_input_frame.pack()

        self.income = Utils.create_entry(tax_bracket_input_frame, 'Income Bracket:')
        self.shortTerm = Utils.create_entry(tax_bracket_input_frame, 'Short Term Bracket:')
        self.longTerm = Utils.create_entry(tax_bracket_input_frame, 'Long Term Bracket:')

    def _make_button(self):
        # TODO: refresh the frame on button press - data on the frames
        button = ttk.Button(self, text='Calculate', style='black.TButton',
                            command=lambda: self.controller.runModel(self))
        button.pack()

    def _make_future_button(self):
        self.future_button = ttk.Button(self, text="Continue", style='black.TButton',
                                        command=lambda: self.controller.showFrame(FutureView.FutureView))
    # endregion

    # region Get Input Parameters (public)
    def get_model_params(self):
        modelParams = ModelParams()
        modelParams.symbol = self.symbol.get()
        modelParams.quantity = self.quantity.get()
        modelParams.purchaseDate = self.purchase_date.get()
        modelParams.transactionCost = self.transaction_cost.get()
        modelParams.db = self.db.get()

        return modelParams

    def get_tax_bracket_params(self):
        brackets = TaxBracketParams()
        brackets.income = self.income.get()
        brackets.shortTerm = self.shortTerm.get()
        brackets.longTerm = self.longTerm.get()

        return brackets
    # endregion

    # region Render (public)
    # TODO Abstract out this method (also in FutureView.py)
    def renderError(self, error):
        self._destroy_frames()
        self.error_frame = tk.Frame(self, bg='yellow')
        self.error_frame.pack()
        tk.Label(self.error_frame, text=error).grid(row=0)

    def renderModel(self):
        self._destroy_frames()
        self._render_model(self.controller.model)
        self._render_tax_bracket(self.controller.taxBracket)
        self._make_future_button()

    def renderCurrentSales(self, currentSales):
        self.regime_frame = tk.Frame(self, bg='blue')
        self.regime_frame.pack()
        tk.Label(self.regime_frame, text="CURRENT SALES").grid(row=0, column=0, columnspan=len(currentSales), pady=PADGRID)
        for i in range(len(currentSales)):
            # currentSales[i].print()
            self._render_current_sale(currentSales[i], i)

    def renderFutureButton(self):
        self.future_button.pack()
    # endregion

    # region Render (private)
    def _destroy_frames(self):
        if self.error_frame is not None:
            self.error_frame.destroy()
        if self.model_response_frame is not None:
            self.model_response_frame.destroy()
        if self.tax_response_frame is not None:
            self.tax_response_frame.destroy()
        if self.regime_frame is not None:
            self.regime_frame.destroy()
        if self.future_button is not None:
            self.future_button.destroy()

    def _render_model(self, model):
        self.model_response_frame = tk.Frame(self, bg='red')
        self.model_response_frame.pack()

        tk.Label(self.model_response_frame, text="MODEL").grid(row=0, column=0, columnspan=SPAN*2, pady=PADGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Symbol: " + model.symbol).grid(row=1, column=0, columnspan=SPAN*2, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Quantity: " + str(model.quantity)).grid(row=2, column=0, columnspan=SPAN*2, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Today: " + str(model.today)).grid(row=3, column=0, columnspan=SPAN, sticky=STICKYGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Current Price: $" + str(model.currentPrice)).grid(row=3, column=SPAN, columnspan=SPAN, sticky=STICKYGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Purchase Date: " + str(model.purchaseDate)).grid(row=4, column=0, columnspan=SPAN, sticky=STICKYGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Purchase Price: $" + str(model.purchasePrice)).grid(row=4, column=SPAN, columnspan=SPAN, sticky=STICKYGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Grant Date: " + str(model.grantDate)).grid(row=5, column=0, columnspan=SPAN, sticky=STICKYGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Grant Price: $" + str(model.grantPrice)).grid(row=5, column=SPAN, columnspan=SPAN, sticky=STICKYGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Exercise Date: " + str(model.exerciseDate)).grid(row=6, column=0, columnspan=SPAN, sticky=STICKYGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Exercise Price: $" + str(model.exercisePrice)).grid(row=6, column=SPAN, columnspan=SPAN, sticky=STICKYGRID, padx=PADGRID)
        tk.Label(self.model_response_frame, text="Discounted Price: " + Utils.formatCurrency(model.discountedPrice)).grid(row=7, column=0, columnspan=SPAN * 2, padx=PADGRID)

    def _render_tax_bracket(self, taxBracket):
        self.tax_response_frame = tk.Frame(self, bg='green')
        self.tax_response_frame.pack()

        tk.Label(self.tax_response_frame, text="TAX BRACKETS").grid(row=0, column=0, columnspan=3, pady=PADGRID)
        tk.Label(self.tax_response_frame, text="Income: " + str(taxBracket.income * 100) + "%").grid(row=1, column=0, padx=PADGRID)
        tk.Label(self.tax_response_frame, text="Short Term: " + str(taxBracket.shortTerm * 100) + "%").grid(row=1, column=1, padx=PADGRID)
        tk.Label(self.tax_response_frame, text="Long Term: " + str(taxBracket.longTerm * 100) + "%").grid(row=1, column=2, padx=PADGRID)

    def _render_current_sale(self, regime, col):
        tk.Label(self.regime_frame, text=f"Regime Type: {regime.regimeType}").grid(row=1, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Date From: {regime.dateFrom}").grid(row=2, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Date To: {regime.dateTo}").grid(row=3, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Sale Proceeds: {Utils.formatCurrency(regime.saleProceeds)}").grid(row=4, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Sale Profit: {Utils.formatCurrency(regime.saleProfit)}").grid(row=5, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Income: {Utils.formatCurrency(regime.income)}").grid(row=6, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Short Term: {Utils.formatCurrency(regime.shortTerm)}").grid(row=7, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Long Term: {Utils.formatCurrency(regime.longTerm)}").grid(row=8, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Tax: {Utils.formatCurrency(regime.tax)}").grid(row=9, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.regime_frame, text=f"Final Proceeds: {Utils.formatCurrency(regime.finalProceeds)}").grid(row=10, column=col, padx=PADGRID, sticky=STICKYGRID)
    # endregion
