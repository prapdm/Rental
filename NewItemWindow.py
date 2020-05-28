# -*- coding: utf-8 -*-
import tkinter as tk
import barcode
from barcode.writer import ImageWriter
from tkinter import *
from tkinter import messagebox
import hashlib
from datetime import datetime
from fpdf import FPDF
import os
from pathlib import Path

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

    def generate_ean(self, ean_number):
        barCodeImage = barcode.get('ean13', ean_number, writer=ImageWriter())
        filename = barCodeImage.save('assets/'+ean_number)
        return filename


    def save(self, name, quanity):
        # sprawdzamy czy pola nie sa puste
        if len(name) == 0 or len(quanity) == 0:
            messagebox.showwarning(title="Information", message="Fill all fields.")
            return False

        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # generowanie numeru ean na podstawie nazwy
        hash1 = hashlib.sha1()
        hash1.update(str(name).encode('utf-8'))
        ean = str(int(hash1.hexdigest(), 16))[:13]

        # metoda generate_ean
        image = self.generate_ean(ean)


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

        answer = messagebox.askquestion("Title", "Do you want print item card?")

        if answer == "yes":
            print(image)
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()
            pdf.rect(40, 30, 90, 50)
            pdf.set_font("Arial", size=11)
            pdf.cell(150, 125,name, 0, 0, 'C')
            pdf.image(image, 60, 40, 50)
            my_file = Path('assets/'+name+".pdf")
            pdf.output(my_file)
            os.startfile(my_file)

            self.close_windows()


        elif answer == "no":
            self.close_windows()

    def print(self):
        return


    def close_windows(self):
        self.master.destroy()
