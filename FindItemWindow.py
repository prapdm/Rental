# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from ResultItemWindow import ResultItemWindow


class FindItemWindow:
    def __init__(self, cnx):
        master = tk.Tk()
        tk.Frame(master)
        master.title("Find Item")
        self.master = master
        self.cnx = cnx


        # pole imie
        tk.Label(master, text="Name:").grid(row=0, sticky=W, padx=10, pady=5)
        name = tk.Entry(master, bd=1)
        name.grid(row=0, column=1, padx=20, pady=5)

        # pole nazwisko
        tk.Label(master, text="Ean:").grid(row=1, sticky=W, padx=10, pady=5)
        ean = tk.Entry(master, bd=1)
        ean.grid(row=1, column=1, padx=20, pady=5)

        # przycisk anuluj
        tk.Button(master, text='Cancel', height=2, width=15, command=self.close_windows).grid(row=2, column=0, padx=10, pady=5)

        # przycisk szukaj
        tk.Button(master, text='Search', height=2, width=15, command=lambda: self.search_item(name.get(), ean.get())).grid(row=2, column=1, padx=10, pady=5)

    def search_item(self, name, ean):

        if self.cnx.is_connected() != True:
        # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # poczatek zapytania SQL
        zapytanie = "SELECT * FROM items "

        if len(name) == 0:
            zapytanie += "WHERE name LIKE \"%%\" "
        else:
            zapytanie += "WHERE name LIKE \"%" + name + "%\" "

        if len(ean) > 0:
            zapytanie += "AND ean =" + ean + " "

        # zapytanie += "ORDER BY name ASC"
        print(zapytanie)

        # odpytaj baze
        cursor = self.cnx.cursor()
        cursor.execute(zapytanie)
        records = cursor.fetchall()

        # otworzmy nowe okno z wynikami
        ResultItemWindow(self.cnx, records)
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()