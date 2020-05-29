# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *

class FindUserWindow:
    def __init__(self, cnx):
        master = tk.Tk()
        tk.Frame(master)
        master.title("Search User")
        self.master = master
        self.cnx = cnx

        # pole imie
        tk.Label(master, text="Name:").grid(row=0, sticky=W, padx=10, pady=5)
        name = tk.Entry(master, bd=1)
        name.grid(row=0, column=1, padx=20, pady=5)

        # pole nazwisko
        tk.Label(master, text="Surname:").grid(row=1, sticky=W, padx=10, pady=5)
        surname = tk.Entry(master, bd=1)
        surname.grid(row=1, column=1, padx=20, pady=5)

        # pole adres
        tk.Label(master, text="Adress:").grid(row=2, sticky=W, padx=10, pady=5)
        adress = tk.Entry(master, bd=1)
        adress.grid(row=2, column=1, padx=20, pady=5)

        # pole telefon
        tk.Label(master, text="Phone:").grid(row=3, sticky=W, padx=10, pady=5)
        phone = tk.Entry(master, bd=1)
        phone.grid(row=3, column=1, padx=20, pady=5)

        # pole email
        tk.Label(master, text="Email:").grid(row=4, sticky=W, padx=10, pady=5)
        email = tk.Entry(master, bd=1)
        email.grid(row=4, column=1, padx=20, pady=5)

        # pole ean
        tk.Label(master, text="EAN:").grid(row=5, sticky=W, padx=10, pady=5)
        ean = tk.Entry(master, bd=1)
        ean.grid(row=5, column=1, padx=20, pady=5)

        # przycisk anuluj
        tk.Button(master, text='Cancel', height=2, width=15, command=self.close_windows).grid(row=6, column=0, padx=10, pady=5)

        # przycisk szukaj
        tk.Button(master, text='Search', height=2, width=15, command=self.close_windows).grid(row=6, column=1, padx=10, pady=5)

    # def search_user(self, name, surname, adress, phone, email,ean):

        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        zapytanie_sql = "SELECT * FROM users "



    def close_windows(self):
        self.master.destroy()
