# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *

class ReturnRentWindow:
    def __init__(self, cnx):
        master = tk.Tk()
        tk.Frame(master)
        master.title("Return / Rent")
        self.master = master
        self.cnx = cnx

        # pole kod EAN
        tk.Label(master, text="EAN:").grid(row=0, sticky=W, padx=10, pady=5)
        name = tk.Entry(master, bd=1)
        name.grid(row=0, column=1, padx=20, pady=5)

        # pole ilosc
        tk.Label(master, text="Quantity:").grid(row=1, sticky=W, padx=10, pady=5)
        surname = tk.Entry(master, bd=1)
        surname.grid(row=1, column=1, padx=20, pady=5)

        # pole ilosc dni
        tk.Label(master, text="Number of days:").grid(row=2, sticky=W, padx=10, pady=5)
        adress = tk.Entry(master, bd=1)
        adress.grid(row=2, column=1, padx=20, pady=5)

        # przycisk ok
        przycisk_zatwierdz = tk.Button(master, text='Confirm', height=2, width=15, command=self.close_windows)
        przycisk_zatwierdz.grid(row=3, column=0, padx=10, pady=5)

        # przycisk anuluj
        przycisk_zatwierdz = tk.Button(master, text='Exit', height=2, width=15, command=self.close_windows)
        przycisk_zatwierdz.grid(row=3, column=1, padx=10, pady=5)

    def close_windows(self):
        self.master.destroy()