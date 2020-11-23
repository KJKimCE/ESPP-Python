from Tools import Utils
from Model.FutureSale import FutureSale, Benefit
import View.ModelView as ModelView
import tkinter as tk
from tkinter import ttk

PADGRID = 5
STICKYGRID = 'W'
SPAN = 2


class FutureView(tk.Frame):
    error_frame = None
    future_response_frame = None
    decision_frame = None

    # region Initialize
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self, parent_frame)
        self.controller = controller

        self._make_future_frame()
        self._make_buttons()
    # endregion

    # region Make Frames (private)
    def _make_future_frame(self):
        top_frame = tk.Frame(self)
        top_frame.pack()
        tk.Label(top_frame, text='Enter Future Date').pack()

        future_frame = tk.Frame(self)
        future_frame.pack()
        self.future_date = Utils.create_entry(future_frame, 'Enter Future Date (yyyymmdd):')

    def _make_buttons(self):
        back = ttk.Button(self, text='Back', style='black.TButton',
                          command=lambda: self.controller.showFrame(ModelView.ModelView))
        back.pack()

        # TODO: refresh the frame on button press - data on the frames
        button = ttk.Button(self, text='Calculate', style='black.TButton',
                            command=lambda: self.controller.runFuture(self))
        button.pack()
    # endregion

    # region Get Input Parameters (public)
    def getFutureDate(self):
        return self.future_date.get()
    # endregion

    # region Render (public)
    # TODO Abstract out this method (also in ModelView.py)
    def renderError(self, error):
        self._destroy_frames()
        self.error_frame = tk.Frame(self, bg='yellow')
        self.error_frame.pack()
        tk.Label(self.error_frame, text=error).grid(row=0)

    def renderFutureSale(self, future):
        self._destroy_frames()
        self.future_response_frame = tk.Frame(self, bg='red')
        self.future_response_frame.pack()
        self._render_future_sale(future, 0)

        for i in range(len(future.benefits)):
            self._render_benefit(future.benefits[i], i + 1)

        self._render_decision(future)
    # endregion

    # region Render (private)
    def _destroy_frames(self):
        if self.error_frame is not None:
            self.error_frame.destroy()
        if self.future_response_frame is not None:
            self.future_response_frame.destroy()
        if self.decision_frame is not None:
            self.decision_frame.destroy()

    def _render_future_sale(self, future: FutureSale, col):
        tk.Label(self.future_response_frame, text="FUTURE SALE").grid(row=0, column=col, pady=PADGRID, padx=PADGRID)
        tk.Label(self.future_response_frame, text=f"Regime Type: {future.regime.regimeType}").grid(row=1, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Date: {future.date}").grid(row=2, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Predicted Price: {Utils.formatCurrency(future.predictedPrice)}").grid(row=3, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Proceeds: {Utils.formatCurrency(future.regime.saleProceeds)}").grid(row=4, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Profit: {Utils.formatCurrency(future.regime.saleProfit)}").grid(row=5, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Income: {Utils.formatCurrency(future.regime.income)}").grid(row=6, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Short Term: {Utils.formatCurrency(future.regime.shortTerm)}").grid(row=7, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Long Term: {Utils.formatCurrency(future.regime.longTerm)}").grid(row=8, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Tax: {Utils.formatCurrency(future.regime.tax)}").grid(row=9, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Final Proceeds: {Utils.formatCurrency(future.regime.finalProceeds)}").grid(row=10, column=col, padx=PADGRID, sticky=STICKYGRID)

    def _render_benefit(self, benefit: Benefit, col):
        tk.Label(self.future_response_frame, text="DIVERSIFICATION BENEFIT").grid(row=0, column=col, pady=PADGRID, padx=PADGRID)
        tk.Label(self.future_response_frame, text=f"Regime Type: {benefit.regimeType}").grid(row=1, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Diversification Benefit: {Utils.formatCurrency(benefit.diversificationBenefit)}").grid(row=2, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Past Proceeds: {Utils.formatCurrency(benefit.pastProceeds)}").grid(row=3, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Final Proceeds: {Utils.formatCurrency(benefit.finalProceeds)}").grid(row=4, column=col, padx=PADGRID, sticky=STICKYGRID)
        tk.Label(self.future_response_frame, text=f"Difference: {Utils.formatCurrency(benefit.difference)}").grid(row=5, column=col, padx=PADGRID, sticky=STICKYGRID)

    def _render_decision(self, future):
        self.decision_frame = tk.Frame(self, bg='blue')
        self.decision_frame.pack()
        tk.Label(self.decision_frame, text=f"Decision: {future.decision}").grid(row=0)

    # endregion
