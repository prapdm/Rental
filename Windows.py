# -*- coding: utf-8 -*-
from MainWindow import MainWindow
from SetupWindow import SetupWindow
from pathlib import Path
import mysql.connector
from mysql.connector import errorcode

class Windows:
    # konstruktor
    def __init__(self):
        # plik gdzie będziemy przechowywać dane do bazy sql
        filename = "database.cfg"
        my_file = Path(filename)
        if my_file.is_file():
            # pusta lista
            lines = []
            # otwieramy plik w trybie do odczytu
            config = open(filename, "r")
            # pętla przez każdą linię
            for line in config:
                lines.append(line)
            print(len(lines))
            # jestli plik nie jest pusty (minimum 5 lini) sprawdź połączenie
            if len(lines) == 5:

                user = lines[0].rstrip()
                password = lines[1].rstrip()
                host = lines[2].rstrip()
                database = lines[3].rstrip()
                port = lines[4].rstrip()
                # zanim odpalimy główne okno sprawdzmy czy jest połączenie z bazą.
                try:
                    cnx = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)

                    if cnx.is_connected:
                        # jest połaczenie odpal główne okno
                        print("Connected - main window")
                        self.show_main_window(cnx)
                    else:
                        # nie ma połączenia - okno setup
                        self.show_setup_window()
                except mysql.connector.Error as err:
                    print(err.errno)
                    self.show_setup_window()

            else:
                 # plik nie ma wszystkich danych
                 self.show_setup_window()

        else:
            # plik nie ma wszystkich danych
            self.show_setup_window()

    # glówne okno programu
    def show_main_window(self, cnx):
        MainWindow(cnx)

    # okno do wprowadzania danych niezbędnych do połączenia z bazą danych
    def show_setup_window(self):
        SetupWindow()

