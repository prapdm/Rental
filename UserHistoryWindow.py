# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk

class UserHistoryWindow:
    def __init__(self, cnx, id):
        master = tk.Tk()
        tk.Frame(master)
        master.title("User History")
        self.master = master
        self.cnx = cnx

        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # poczatek zapytania SQL
        zapytanie = "SELECT * FROM rentals LEFT JOIN items ON rentals.item_id = items.id WHERE rentals.user_id = " + str(id) + " ORDER BY rentals.id ASC"
        print(zapytanie)

        # odpytaj baze
        cursor = self.cnx.cursor()
        cursor.execute(zapytanie)
        records = cursor.fetchall()

        self.show_table(records)


    def close_windows(self):
        self.master.destroy()

    def show_table(self,records):
        # tworzymy tabele i naglowki
        cols = ('ID', 'Name', 'Quantity', 'Rented', "To", 'Returned')
        table = ttk.Treeview(self.master, columns=cols, show='headings')
        table.grid(row=2, columnspan=1, sticky=N + S + W + E)
        for col in cols:
            table.heading(col, text=col)

        #szerokość kolumn
        table.column(cols[0], anchor='center', width=50)
        table.column(cols[1], anchor='center', width=300)
        table.column(cols[2], anchor='center', width=150)
        table.column(cols[3], anchor='center', width=300)
        table.column(cols[4], anchor='center', width=300)
        table.column(cols[5], anchor='center', width=300)

        # wstawiamy dane
        for row in records:
            table.insert("", "end", values=(row[0], row[10], row[3], row[4], row[5], row[6]))


        # tworzymy suwak boczny
        scroll = ttk.Scrollbar(self.master)
        scroll.grid(row=2, column=1, sticky="nse")  # set this to column=2 so it sits in the correct spot.
        scroll.configure(command=table.yview)
        table.configure(yscrollcommand=scroll.set)