# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta

class RentWindow:
    def __init__(self, cnx, id):
        master = tk.Tk()
        tk.Frame(master)
        master.title("Rent")
        self.master = master
        self.cnx = cnx

        # pole kod EAN
        tk.Label(master, text="EAN:").grid(row=0, sticky=W, padx=10, pady=5)
        self.ean = tk.Entry(master, bd=1)
        self.ean.grid(row=0, column=1, padx=20, pady=5)

        # pole ilosc
        tk.Label(master, text="Quantity:").grid(row=1, sticky=W, padx=10, pady=5)
        self.quanity = tk.Entry(master, bd=1)
        self.quanity.grid(row=1, column=1, padx=20, pady=5)

        # pole na ile dni
        tk.Label(master, text="Days:").grid(row=2, sticky=W, padx=10, pady=5)
        self.days = tk.Entry(master, bd=1)
        self.days.grid(row=2, column=1, padx=20, pady=5)

        # przycisk ok
        przycisk_zatwierdz = tk.Button(master, text='Confirm', height=2, width=15, command=lambda: self.renting(self.ean.get(), self.quanity.get(), self.days.get(), id))
        przycisk_zatwierdz.grid(row=4, column=1, padx=10, pady=5)

        # przycisk anuluj
        przycisk_zatwierdz = tk.Button(master, text='Exit', height=2, width=15, command=self.close_windows)
        przycisk_zatwierdz.grid(row=4, column=0, padx=10, pady=5)

    def close_windows(self):
        self.master.destroy()

    def renting(self,ean, quanity, days, user_id):
        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # sprawdzamy czy pola nie sa puste
        if len(ean) == 0 or len(quanity) == 0 or len(days) == 0 :
            messagebox.showwarning(title="Information", message="Fill all fields.")
            return False

        # poczatek zapytania SQL
        zapytanie = "SELECT * FROM `items` WHERE `ean` = " + str(ean) + " LIMIT 1"
        print(zapytanie)

        # odpytaj baze
        cursor = self.cnx.cursor()
        cursor.execute(zapytanie)
        records = cursor.fetchall()

        # sprawdzamy czy taki kod EAN istnieje w bazie
        if len(records) == 0 :
            messagebox.showwarning(title="Information", message="There is no item with this EAN number.")
            return False
        else:
            # sprawdźmy czy może wypożyczyć wiecej niż może
            for row in records:
                if int(quanity) == 0:
                    messagebox.showwarning(title="Information", message="You have to rent 1 item minimum")
                    return False

                if int(quanity) > row[2]:
                    messagebox.showwarning(title="Information", message="You can't rent more them "+row[2]+" items")
                    return False

                if int(days) == 0 :
                    messagebox.showwarning(title="Information", message="You have to rent for one day minimum")
                    return False

                # Wszystkie warunki spełnione, wypożyczmy
                now = datetime.now()
                date_to = now + timedelta(days=int(days))

                rent_item = ("INSERT INTO rentals"
                               "(user_id, item_id, quanity, rent, to_date, created_at)"
                               "VALUES (%(user_id)s, %(item_id)s, %(quanity)s, %(rent)s, %(to_date)s,  %(created_at)s )")

                data_rent_item = {
                    'user_id': user_id,
                    'item_id': str(row[0]),
                    'quanity': str(quanity),
                    'rent': now.strftime("%Y-%m-%d %H:%M:%S"),
                    'to_date': date_to.strftime("%Y-%m-%d %H:%M:%S"),
                    'created_at': now.strftime("%Y-%m-%d %H:%M:%S"),
                }

                print(data_rent_item)
                cursor.execute(rent_item, data_rent_item)
                # Make sure data is committed to the database
                self.cnx.commit()

                self.close_windows()