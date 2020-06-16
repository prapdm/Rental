# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter import messagebox

class ReturnRentWindow:
    def __init__(self, cnx, id):
        master = tk.Tk()
        tk.Frame(master)
        master.title("Return / Rent")
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


        # przycisk ok
        przycisk_zatwierdz = tk.Button(master, text='Confirm', height=2, width=15,   command=lambda : self.returning(self.ean.get(), self.quanity.get(), id))
        przycisk_zatwierdz.grid(row=3, column=1, padx=10, pady=5)

        # przycisk anuluj
        przycisk_zatwierdz = tk.Button(master, text='Exit', height=2, width=15, command=self.close_windows)
        przycisk_zatwierdz.grid(row=3, column=0, padx=10, pady=5)

    def close_windows(self):
        self.master.destroy()

    def returning(self,ean, quanity, user_id):
        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # sprawdzamy czy pola nie sa puste
        if len(self.ean.get()) == 0 or len(self.quanity.get()) == 0 :
            messagebox.showwarning(title="Information", message="Fill all fields.")
            return False



        # poczatek zapytania SQL
        zapytanie = "SELECT * FROM rentals LEFT JOIN items ON rentals.item_id = items.id LEFT JOIN users ON rentals.user_id = users.id WHERE items.ean = " + str(ean) + " AND users.id = "+str(user_id)+"  LIMIT 1"
        print(zapytanie)

        # odpytaj baze
        cursor = self.cnx.cursor()
        cursor.execute(zapytanie)
        records = cursor.fetchall()
        # Make sure data is committed to the database
        self.cnx.commit()





        if len(records) == 0:
            messagebox.showwarning(title="Information", message="You did not borrow this item")
            return False


        for row in records:
            now = datetime.now()
            quanity_left = int(row[3]) - int(quanity)
            if(quanity_left<0):
                messagebox.showwarning(title="Information", message="You haven't rented that much")
                return False
            else:
                add_history = ("INSERT INTO rentals"
                            "(user_id, item_id, quanity, rent, to_date, returned, created_at)"
                            "VALUES (%(user_id)s, %(item_id)s, %(quanity)s, %(rent)s, %(to_date)s, %(returned)s, %(created_at)s )")

                data_history = {
                    'user_id': user_id,
                    'item_id': str(row[9]),
                    'quanity': str(quanity),
                    'rent': str(row[4]),
                    'to_date': str(row[5]),
                    'returned': now.strftime("%Y-%m-%d %H:%M:%S"),
                    'created_at': str(row[7]),
                }

                print(add_history)
                cursor.execute(add_history, data_history)
                # Make sure data is committed to the database
                self.cnx.commit()




        self.close_windows()