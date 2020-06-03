# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk

class ResultItemWindow:
    def __init__(self, cnx, records):
        master = tk.Tk()
        tk.Frame(master)
        master.title("Results Item")
        self.master = master
        self.cnx = cnx

        Checkbutton(master, text="rented:", variable=1).grid(row=1, column=0, sticky=W)
        Checkbutton(master, text="expired:", variable=1).grid(row=2, column=0, sticky=W)

        v1 = StringVar(master, value='1')
        q1 = tk.Entry(master, bd=1, textvariable=v1)
        q1.grid(row=1, column=0, padx=75, pady=5, sticky=W)
        v2 = StringVar(master, value='1')
        q2 = tk.Entry(master, bd=1, textvariable=v2)
        q2.grid(row=2, column=0, padx=75, pady=5, sticky=W)



        self.show_table(records)

    def close_windows(self):
        self.master.destroy()

    def show_table(self,records):
        # tworzymy tabele i naglowki
        cols = ('ID', 'Name', 'Quanity', 'EAN')
        table = ttk.Treeview(self.master, columns=cols, show='headings')
        for col in cols:
            table.heading(col, text=col)

        #szerokość kolumn
        table.column(cols[0], anchor='center', width=50)
        table.column(cols[1], anchor='center', width=300)
        table.column(cols[2], anchor='center', width=50)
        table.column(cols[3], anchor='center', width=250)


        # wstawiamy dane
        for row in records:
            table.insert("", "end", values=(row[0], row[1], row[2], row[3]))

        # siatka
        table.grid(row=4, column=0, padx=0, pady=0)

        return table

    def destroy_table(self,table):
        table.delete()