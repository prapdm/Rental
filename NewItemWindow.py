# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

class NewItemWindow:
    def __init__(self, cnx):
        master = tk.Tk()
        tk.Frame(master)
        master.title("New Item")
        self.master = master
        self.cnx = cnx

        # pole nazwa
        tk.Label(master, text="Name:").grid(row=0, sticky=W, padx=10, pady=5)
        name = tk.Entry(master, bd=1)
        name.grid(row=0, column=1, padx=20, pady=5)

        # pole ilosc
        tk.Label(master, text="Quanity:").grid(row=1, sticky=W, padx=10, pady=5)
        quanity = tk.Entry(master, bd=1)
        quanity.grid(row=1, column=1, padx=20, pady=5)

        # przycisk anuluj
        tk.Button(master, text='Cancel', height=2, width=15, command=self.close_windows).grid(row=3, column=0, padx=10, pady=5)

        # przycisk zapisz
        tk.Button(master, text='Save', height=2, width=15, command=lambda : self.save(name.get(), quanity.get())).grid(row=3, column=1, padx=10, pady=5)

    # metody

    def save(self, name, quanity):
        # sprawdzamy czy pola nie sa puste
        if len(name) == 0 or len(quanity) == 0:
            messagebox.showwarning(title="Information", message="Fill all fields.")
            return False

        if self.cnx.is_connected != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect


        # zapisz dane do bazy - metoda save()
        cursor = self.cnx.cursor()
        add_item = ("INSERT INTO items"
                    "(name, quanity, created_at)"
                    "VALUES (%(name)s, %(quanity)s, %(created_at)s)")

        # aktualna data i czas
        now = datetime.now()

        data_item = {
            'name': name,
            'quanity': quanity,
            'created_at': now,
        }

        # dodajmy do bazy
        cursor.execute(add_item, data_item)

        # Make sure data is committed to the database
        self.cnx.commit()

        # rozlacz z bazą
        cursor.close()
        self.cnx.close()

        answer = messagebox.askquestion("Title", "Are you sure you want to save?")

        if answer == "yes":
            self.close_windows()

        elif answer == "no":
            self.close_windows()

    def print(self):
        return


    def close_windows(self):
        self.master.destroy()
