# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from UserEditWindow import UserEditWindow
from UserHistoryWindow import UserHistoryWindow
from ReturnRentWindow import ReturnRentWindow

class UserWindow:
    def __init__(self, cnx, id):
        master = tk.Tk()
        tk.Frame(master)
        master.title("User's File")
        self.master = master
        self.cnx = cnx
        self.id = id

        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # poczatek zapytania SQL
        zapytanie = "SELECT * FROM users WHERE id = " + str(id) + " LIMIT 1"
        print(zapytanie)

        # odpytaj baze
        cursor = self.cnx.cursor()
        cursor.execute(zapytanie)
        records = cursor.fetchall()


        for row in records:
            # label imie
            imie_label = tk.Label(master, text="Name:")
            imie_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)

            # pole imie
            imie_var = StringVar(master, value=row[1])
            imie = tk.Entry(master, bd=1, textvariable=imie_var)
            imie.config(state='disabled')
            imie.grid(row=0, column=1, padx=20, pady=5)

            # label nazwisko
            nazwisko_label = tk.Label(master, text="Surname:")
            nazwisko_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)

            # pole nazwisko
            nazwisko_var = StringVar(master, value=row[2])
            nazwisko = tk.Entry(master, bd=1, textvariable=nazwisko_var)
            nazwisko.config(state='disabled')
            nazwisko.grid(row=1, column=1, padx=20, pady=5)

            # label adres
            adres_label = tk.Label(master, text="Adress:")
            adres_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)

            # pole adres
            adres_var = StringVar(master, value=row[3])
            adres = tk.Entry(master, bd=1,textvariable=adres_var)
            adres.config(state='disabled')
            adres.grid(row=2, column=1, padx=20, pady=5)

            # label telefon
            phone_label = tk.Label(master, text="Phone:")
            phone_label.grid(row=3, column=0, sticky=W, padx=10, pady=5)

            # pole telefon
            phone_var = StringVar(master, value=row[4])
            phone = tk.Entry(master, bd=1,textvariable=phone_var)
            phone.config(state='disabled')
            phone.grid(row=3, column=1, padx=20, pady=5)

            # label email
            email_label = tk.Label(master, text="Email:")
            email_label.grid(row=4, column=0, sticky=W, padx=10, pady=5)

            # pole email
            email_var = StringVar(master, value=row[5])
            email = tk.Entry(master, bd=1,textvariable=email_var)
            email.config(state='disabled')
            email.grid(row=4, column=1, padx=20, pady=5)

            # pole ean
            ean_label = tk.Label(master, text="Ean:")
            ean_label.grid(row=5, column=0, sticky=W, padx=10, pady=5)

            # pole ean
            ean_var = StringVar(master, value=row[6])
            ean = tk.Entry(master, bd=1,textvariable=ean_var)
            ean.config(state='disabled')
            ean.grid(row=5, column=1, padx=20, pady=5)

        # przycisk zwrot
        przycisk_zwrot = tk.Button(master, text='Return', height=2, width=15, command=self.reurned_item)
        przycisk_zwrot.grid(row=6, column=0, padx=10, pady=5)

        # przycisk wypożyczenia
        przycisk_wypozycz = tk.Button(master, text='Rent', height=2, width=15, command=self.rent_item)
        przycisk_wypozycz.grid(row=6, column=1, padx=10, pady=5)

        # przycisk historia
        przycisk_historia = tk.Button(master, text='History', height=2, width=15, command=self.history_user)
        przycisk_historia.grid(row=7, column=0, padx=10, pady=5)

        # przycisk edycja danych
        przycisk_edycja = tk.Button(master, text='Edit Data', height=2, width=15, command=self.edit_user)
        przycisk_edycja.grid(row=7, column=1, padx=10, pady=5)

    def close_windows(self):
        self.master.destroy()


    def edit_user(self):
        UserEditWindow(self.cnx , self.id)


    def history_user(self):
        UserHistoryWindow(self.cnx , self.id)

    def rent_item(self):
        ReturnRentWindow(self.cnx , self.id)

    def reurned_item(self):
        ReturnRentWindow(self.cnx, self.id)
