# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import mysql.connector
from mysql.connector import errorcode
from pathlib import Path

class SetupWindow():

    def __init__(self):
        master = tk.Tk()
        master.title("Setup database connection")
        master.resizable(False, False)
        window_height = 250
        window_width = 295
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # pole adres
        tk.Label(master, text="Address").grid(row=0, sticky=W, padx=10, pady=5)
        address = tk.Entry(master, bd=1)
        address.grid(row=0, column=1, padx=20, pady=5)


        # pole port
        tk.Label(master, text="Port").grid(row=1, sticky=W, padx=10, pady=5)
        # domyslna wartosc portu 3306
        v = StringVar(master, value='3306')
        port = tk.Entry(master, bd=1, textvariable=v)
        port.grid(row=1, column=1, padx=20, pady=5)

        # pole db user
        tk.Label(master, text="Database user").grid(row=2, sticky=W, padx=10, pady=5)
        user =tk.Entry(master, bd=1)
        user.grid(row=2, column=1, padx=20, pady=5)

        #pole password
        tk.Label(master, text="Password").grid(row=3, sticky=W, padx=10, pady=5)
        password =tk.Entry(master, bd=1, show="*")
        password.grid(row=3, column=1, padx=20, pady=5)

        #pole db name
        tk.Label(master, text="Database name").grid(row=4, sticky=W, padx=10, pady=5)
        dbname =tk.Entry(master, bd=1)
        dbname.grid(row=4, column=1, padx=20, pady=5)

        self.info = tk.StringVar(value="")
        self.infolabel = tk.Label(master, textvariable=self.info)
        self.infolabel.grid(row=5, sticky=W, padx=10, pady=5)

        tk.Button(master, text='Test connection', height=2, width=15, command=lambda : self.test_connection(user.get(), password.get(), address.get(), dbname.get(), port.get())).grid(row=6, column=0, padx=10, pady=5)
        tk.Button(master, text='Save', height=2, width=15, command=lambda : self.save_settings(user.get(), password.get(), address.get(), dbname.get(), port.get())).grid(row=6, column=1, padx=10, pady=5)

        master.mainloop()

    def __del__(self):
        return


    # Test connection method
    def test_connection(self, user, password, host, database, port):
        try:
            cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
            if(cnx.is_connected):
                self.infolabel.config(fg='green')
                self.info.set("Connection OK")
                return True
            else:
                return False
        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.infolabel.config(fg='red')
                self.info.set("Something is wrong with your name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.infolabel.config(fg='red')
                self.info.set("Database does not exist")
            else:
                self.infolabel.config(fg ='red')
                self.info.set("Connection error - "+str(err.errno))

        return False


    # Save settings to database.cfg file
    def save_settings(self, user, password, host, database, port):
        # przed zapisem sprawdzmy czy dane są prawidlowe i czy jest polaczenie

        if self.test_connection(user, password, host, database, port):
            # mamy połączenie z bazą zapiszmy dane do bazy

            # sciezka do naszego pliku
            my_file = Path("database.cfg")
            # otwieramy plik do edycji
            config = open(my_file, 'w')
            # zapisujemy dane

            config.write(user+"\n")
            config.write(password+"\n")
            config.write(host+"\n")
            config.write(database+"\n")
            config.write(port + "\n")
            # zamykamy plik
            config.close()
            # zwracamy wartosc
            self.infolabel.config(fg='green')
            self.info.set("OK - need restart" )
        else:
            self.infolabel.config(fg='red')
            self.info.set("Connection error")
