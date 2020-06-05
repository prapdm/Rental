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

        Checkbutton(master, text="users who have borrowed minimum", variable=1).grid(row=0,  column=0, sticky=W)
        Checkbutton(master, text="days after the deadline:", variable=1).grid(row=1, column=0,   sticky=W)

        v1 = StringVar(master, value='1')
        q1 = tk.Entry(master, bd=1, textvariable=v1)
        q1.grid(row=0, column=0, padx=250, pady=5, sticky=W)
        v2 = StringVar(master, value='1')
        q2 = tk.Entry(master, bd=1, textvariable=v2)
        q2.grid(row=1, column=0, padx=250, pady=5, sticky=W)

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

    def destroy_table(self,table):
        table.delete()