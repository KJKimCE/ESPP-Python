import tkinter as tk
import datetime


def formatCurrency(price):
    return "${:,.2f}".format(price)


def validateDate(date):
    try:
        return datetime.datetime.strptime(date, "%Y%m%d").date()
    except ValueError:
        raise ValueError(f"Invalid date: {date}.")


def create_entry(frame, labelText):
    tk.Label(frame, text=labelText).pack(side='left')
    entry = tk.Entry(frame)
    entry.pack(side='left')

    return entry
