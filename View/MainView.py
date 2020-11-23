from View.ModelView import ModelView
from View.FutureView import FutureView
import tkinter as tk
from tkinter import ttk

PAD = 10
HEIGHT = 700
WIDTH = 800


class MainView(tk.Tk):
    main_frame = None

    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.controller = controller

        self._make_main_frame()

        self.frames = {}
        for F in [ModelView, FutureView]:
            frame = F(self.main_frame, controller)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ModelView)
        # self.error_frame = tk.Frame(self.main_frame, bg='yellow')
        # self.error_frame.pack()
        # self.error_label = tk.Label(self.error_frame)
        # self.error_label.grid(row=0)

    def _make_main_frame(self):
        self.title = "ESPP View"
        ttk.Style().configure('black.TButton', foreground='black')
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=PAD, pady=PAD)
        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

    def show_frame(self, container):
        self.frames[container].tkraise()

    def main(self):
        self.mainloop()
