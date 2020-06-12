# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *

class UserHistoryWindow:
    def __init__(self, cnx, records):
        master = tk.Tk()
        tk.Frame(master)
        master.title("User History")
        self.master = master
        self.cnx = cnx

        self.show_table(records)

    def close_windows(self):
        self.master.destroy()

    def show_table(self,records):
        # tworzymy tabele i naglowki
        cols = ('ID', 'Name', 'Quantity', 'Rented', 'Returned')
        table = ttk.Treeview(self.master, columns=cols, show='headings')
        for col in cols:
            table.heading(col, text=col)

