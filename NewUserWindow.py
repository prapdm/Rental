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


class NewUserWindow:
    def __init__(self, master, cnx):
        self.cnx = cnx
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("New User")


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

        # EAN


        # przycisk anuluj
        tk.Button(master, text='Cancel', height=2, width=15, command=self.close_windows).grid(row=5, column=0, padx=10, pady=5)


        # przycisk zapisz
        tk.Button(master, text='Save', height=2, width=15, command=lambda : self.save(name.get(), surname.get(), adress.get(), phone.get(), email.get())).grid(row=5, column=1, padx=10, pady=5)

    def generate_ean(self, ean_number):
        barCodeImage = barcode.get('ean13', ean_number, writer=ImageWriter())
        filename = barCodeImage.save('assets/'+ean_number)
        return filename


    def save(self, name, surname, adress, phone, email):

        # sprawdzamy czy pola nie sa puste
        if len(name) == 0 or len(surname) == 0 or len(adress) == 0 or len(phone) == 0 or len(email) == 0:
            messagebox.showwarning(title="Information", message="Fill all fields.")
            return False


        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # generowanie numeru ean na podstawie imienia i nazwiska
        hash1 = hashlib.sha1()
        hash1.update(str(name + surname).encode('utf-8'))
        ean = str(int(hash1.hexdigest(), 16))[:13]

        # metoda generate_ean
        image = self.generate_ean(ean)

        # zapisz dane do bazy - metoda save()
        cursor = self.cnx.cursor()
        add_user = ("INSERT INTO users"
                    "(name, surname, adress, phone, email, ean, created_at)"
                    "VALUES (%(name)s, %(surname)s, %(adress)s, %(phone)s, %(email)s, %(ean)s, %(created_at)s)")

        # aktualna data i czas
        now = datetime.now()

        data_user = {
            'name': name,
            'surname': surname,
            'adress': adress,
            'phone': phone,
            'email': email,
            'ean': int(ean),
            'created_at': now,
                    }

        # dodajmy do bazy
        cursor.execute(add_user, data_user)

        # Make sure data is committed to the database
        self.cnx.commit()

        # rozlacz z bazą
        cursor.close()
        self.cnx.close()

        answer = messagebox.askquestion("Title", "Do you want print user card?")

        if answer == "yes":
            print(image)
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()
            pdf.rect(40,30,90,50)
            pdf.set_font("Arial", size=11)
            pdf.cell(150,125,name+" "+surname,0,0,'C')
            pdf.image(image, 60, 40, 50)
            my_file = Path('assets/'+name+"_"+surname+".pdf")
            pdf.output(my_file)
            os.startfile(my_file)

            self.close_windows()

        elif answer == "no":
            self.close_windows()

    def print(self):
        return


    def close_windows(self):
        self.master.destroy()

