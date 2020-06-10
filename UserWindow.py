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




        # przycisk usun z systemu
        przycisk_usun = tk.Button(master, text='Remove from base', height=2, width=15, command=self.close_windows)
        przycisk_usun.grid(row=6, column=0, padx=10, pady=5)

        # przycisk potwierdzenie zapisu
        przycisk_zapis = tk.Button(master, text='Save changes', height=2, width=15, command=self.close_windows)
        przycisk_zapis.grid(row=6, column=1, padx=10, pady=5)


    def close_windows(self):
        self.master.destroy()


