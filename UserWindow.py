# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *

class UserWindow:
    def __init__(self, cnx):
        master = tk.Tk()
        tk.Frame(master)
        master.title("User Window")
        self.master = master
        self.cnx = cnx

        # label imie
        imie_label = tk.Label(master, text="Name:")
        imie_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)

        # pole imie
        imie = tk.Entry(master, bd=1)
        imie.config(state='disabled')
        imie.grid(row=0, column=1, padx=20, pady=5)

        # label nazwisko
        nazwisko_label = tk.Label(master, text="Surname:")
        nazwisko_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)

        # pole nazwisko
        nazwisko = tk.Entry(master, bd=1)
        nazwisko.config(state='disabled')
        nazwisko.grid(row=1, column=1, padx=20, pady=5)

        # pole adres
        adres_label = tk.Label(master, text="Adress:")
        adres_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)

        # pole nadres
        adres = tk.Entry(master, bd=1)
        adres.config(state='disabled')
        adres.grid(row=2, column=1, padx=20, pady=5)

        # pole telefon
        phone_label = tk.Label(master, text="Phone:")
        phone_label.grid(row=3, column=0, sticky=W, padx=10, pady=5)

        # pole telefon
        phone = tk.Entry(master, bd=1)
        phone.config(state='disabled')
        phone.grid(row=3, column=1, padx=20, pady=5)

        # pole email
        email_label = tk.Label(master, text="Email:")
        email_label.grid(row=4, column=0, sticky=W, padx=10, pady=5)

        # pole email
        email = tk.Entry(master, bd=1)
        email.config(state='disabled')
        email.grid(row=4, column=1, padx=20, pady=5)

        # pole ean
        ean_label = tk.Label(master, text="Ean:")
        ean_label.grid(row=5, column=0, sticky=W, padx=10, pady=5)

        # pole ean
        ean = tk.Entry(master, bd=1)
        ean.config(state='disabled')
        ean.grid(row=5, column=1, padx=20, pady=5)

        # przycisk usun z systemu
        przycisk_usun = tk.Button(master, text='Remove from base', height=2, width=15, command=self.close_windows)
        przycisk_usun.grid(row=6, column=0, padx=10, pady=5)

        # przycisk potwierdzenie zapisu
        przycisk_zapis = tk.Button(master, text='Save changes', height=2, width=15, command=self.close_windows)
        przycisk_zapis.grid(row=6, column=1, padx=10, pady=5)


    def close_windows(self):
        self.master.destroy()


