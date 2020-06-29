# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *

class UserEditWindow:
    def __init__(self, cnx, id):
        master = tk.Tk()
        tk.Frame(master)
        master.title("User Window")
        self.master = master
        self.cnx = cnx


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
            self.imie = tk.Entry(master, bd=1, textvariable=imie_var)
            self.imie.grid(row=0, column=1, padx=20, pady=5)

            # label nazwisko
            nazwisko_label = tk.Label(master, text="Surname:")
            nazwisko_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)

            # pole nazwisko
            nazwisko_var = StringVar(master, value=row[2])
            self.nazwisko = tk.Entry(master, bd=1, textvariable=nazwisko_var)
            self.nazwisko.grid(row=1, column=1, padx=20, pady=5)

            # label adres
            adres_label = tk.Label(master, text="Adress:")
            adres_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)

            # pole adres
            adres_var = StringVar(master, value=row[3])
            self.adres = tk.Entry(master, bd=1,textvariable=adres_var)
            self.adres.grid(row=2, column=1, padx=20, pady=5)

            # label telefon
            phone_label = tk.Label(master, text="Phone:")
            phone_label.grid(row=3, column=0, sticky=W, padx=10, pady=5)

            # pole telefon
            phone_var = StringVar(master, value=row[4])
            self.phone = tk.Entry(master, bd=1,textvariable=phone_var)
            self.phone.grid(row=3, column=1, padx=20, pady=5)

            # label email
            email_label = tk.Label(master, text="Email:")
            email_label.grid(row=4, column=0, sticky=W, padx=10, pady=5)

            # pole email
            email_var = StringVar(master, value=row[5])
            self.email = tk.Entry(master, bd=1,textvariable=email_var)
            self.email.grid(row=4, column=1, padx=20, pady=5)

            # pole ean
            ean_label = tk.Label(master, text="Ean:")
            ean_label.grid(row=5, column=0, sticky=W, padx=10, pady=5)

            # pole ean
            ean_var = StringVar(master, value=row[6])
            self.ean = tk.Entry(master, bd=1,textvariable=ean_var)
            self.ean.grid(row=5, column=1, padx=20, pady=5)

            # przycisk usun z systemu
            przycisk_usun = tk.Button(master, text='Remove from base', height=2, width=15,  command=lambda: self.confirm_delete(row[0]))
            przycisk_usun.grid(row=6, column=0, padx=10, pady=5)

            # przycisk potwierdzenie zapisu
            przycisk_zapis = tk.Button(master, text='Save changes', height=2, width=15,  command=lambda: self.save_user(row[0]))
            przycisk_zapis.grid(row=6, column=1, padx=10, pady=5)


    def close_windows(self):
        self.master.destroy()


    def delete_user(self, id):
        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # poczatek zapytania SQL
        zapytanie = "DELETE FROM users WHERE id = " + str(id)
        print(zapytanie)

        # wykonaj (skasuj rekord)
        cursor = self.cnx.cursor()
        cursor.execute(zapytanie)

        #zamknij okno
        self.close_windows()


    def save_user(self, id):

        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # sprawdzamy czy pola nie sa puste
        if len(self.imie.get()) == 0 or len(self.nazwisko.get()) == 0 or len(self.adres.get()) == 0 or len(self.phone.get()) == 0 or len(self.email.get()) == 0:
            messagebox.showwarning(title="Information", message="Fill all fields.")
            return False

        # poczatek zapytania SQL
        query = "UPDATE users SET name = '"+str(self.imie.get())+"', surname = '"+str(self.nazwisko.get())+"' , adress = '"+str(self.adres.get())+"' , phone = '"+str(self.phone.get())+"' , email = '"+str(self.email.get())+"' WHERE id = "+str(id)
        print(query)

        # wykonaj
        cursor = self.cnx.cursor()
        cursor.execute(query)

        # Make sure data is committed to the database
        self.cnx.commit()

        #zamknij okno
        self.close_windows()

    def confirm_delete(self, id):
        answer = messagebox.askquestion("Title", "Are you sure you want to save?")
        if answer == "yes":
             self.delete_user(id)
        else:
             self.close_windows()

