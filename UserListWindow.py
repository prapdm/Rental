# -*- coding: utf-8 -*-
import tkinter as tk
from ResultUserWindow import ResultUserWindow


class UserListWindow:
    def __init__(self, cnx):
        master = tk.Tk()
        tk.Frame(master)
        master.title("User List")
        self.master = master
        self.cnx = cnx


    def view_users(self, cnx):

        if self.cnx.is_connected() != True:
            # nie ma polaczenia wiec zrob reconnect
            self.cnx.reconnect()

        # poczatek zapytania SQL
        zapytanie = "SELECT * FROM users ORDER BY name ASC"
        print(zapytanie)

        # odpytaj baze
        cursor = self.cnx.cursor()
        cursor.execute(zapytanie)
        records = cursor.fetchall()
        # Make sure data is committed to the database
        self.cnx.commit()

        # rozlacz z bazą
        cursor.close()

        # otworzmy nowe okno z wynikami
        ResultUserWindow(self.cnx,records, zapytanie)
        self.master.destroy()


    def close_windows(self):
        self.master.destroy()