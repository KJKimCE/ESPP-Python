import tkinter as tk
import datetime


runDate = datetime.date.today()


def formatCurrency(price):
    return "${:,.2f}".format(price)


def formatInt(num, field):
    try:
        return int(num)
    except ValueError:
        raise ValueError(f"Invalid {field}: {num}")


def formatFloat(num, field):
    try:
        return float(num)
    except ValueError:
        raise ValueError(f"Invalid {field}: {num}")


def formatDate(date):
    try:
        return datetime.datetime.strptime(date, "%Y%m%d").date()
    except ValueError:
        raise ValueError(f"Invalid date: {date}")


def create_entry(frame, labelText):
    tk.Label(frame, text=labelText).pack(side='left')
    entry = tk.Entry(frame)
    entry.pack(side='left')

    return entry
