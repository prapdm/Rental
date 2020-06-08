# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk

class ResultUserWindow:
    def __init__(self, cnx, records):
        master = tk.Tk()
        tk.Frame(master)
        master.title("Results User")
        master.state('zoomed')
        # Fix for full with height
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(2, weight=1)


        self.master = master
        self.cnx = cnx

        v1 = StringVar(master, value='1')
        v1.trace("w", lambda name, index, mode, v1=v1: self.filter_1(q1.get()))
        q1 = tk.Entry(master, bd=1, textvariable=v1,state="disabled")
        q1.grid(row=0, column=0, padx=250, pady=5, sticky=W)
        self.q1 = q1

        v2 = StringVar(master, value='1')
        q2 = tk.Entry(master, bd=1, textvariable=v2)
        q2.grid(row=1, column=0, padx=250, pady=5, sticky=W)

        checkbox1 = Checkbutton(master, text="users who have borrowed minimum", variable=1, command=lambda: self.borrowed_days_click( q1.get()))
        checkbox1.grid(row=0,  column=0, sticky=W)
        checkbox2 = Checkbutton(master, text="days after the deadline:", variable=2).grid(row=1, column=0,   sticky=W)

        self.show_table(records)


    def close_windows(self):
        self.master.destroy()

    def show_table(self,records):

        # tworzymy tabele i naglowki
        cols = ('ID', 'Name', 'Surname', 'adress', 'Phone', 'Email', 'EAN', "Created at", "Rented", "Deadline")
        table = ttk.Treeview(self.master, columns=cols,selectmode='browse', show='headings')
        table.grid(row=2, columnspan=1,   sticky=N+S+W+E)


        for col in cols:
            table.heading(col, text=col)

        #szerokość kolumn
        table.column(cols[0], anchor='center', width=50)
        table.column(cols[1], anchor='center', width=100)
        table.column(cols[2], anchor='center', width=150)
        table.column(cols[3], anchor='center', width=300)
        table.column(cols[4], anchor='center', width=100)
        table.column(cols[5], anchor='center', width=200)
        table.column(cols[7], anchor='center', width=120)
        table.column(cols[6], anchor='center', width=50)
        table.column(cols[6], anchor='center', width=50)

        # wstawiamy dane
        for row in records:
            table.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


        # tworzymy suwak boczny
        scroll = ttk.Scrollbar(self.master)
        scroll.grid(row=2, column=1, sticky="nse")  # set this to column=2 so it sits in the correct spot.
        scroll.configure(command=table.yview)
        table.configure(yscrollcommand=scroll.set)

        return table

    def borrowed_days_click(self, days):

        if self.q1["state"] == "disabled":
            self.q1.config(state='normal')
        else:
            self.q1.config(state='disabled')

        self.filter_1(days)


    def filter_1(self, days):

        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        if self.q1["state"] == "normal":
            zapytanie = "SELECT * FROM users LEFT JOIN rentals ON users.id = rentals.user_id WHERE rentals.to_date < CURDATE() -" + days + " ORDER BY name ASC"
        else:
            zapytanie = "SELECT * FROM users ORDER BY name ASC"

        print(zapytanie)

        # odpytaj baze
        cursor = self.cnx.cursor()
        cursor.execute(zapytanie)
        records = cursor.fetchall()

        self.show_table(records)


