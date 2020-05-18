from MainWindow import MainWindow
from SetupWindow import SetupWindow
from pathlib import Path


class Windows:
    # konstruktor
    def __init__(self):
        # plik gdzie będziemy przechowywać dane do bazy sql
        my_file = Path("database.cfg")
        if my_file.is_file():
            self.show_main_window()
        else:
            self.show_setup_window()

    # glówne okno programu
    def show_main_window(self):
        MainWindow()

    # okno do wprowadzania danych niezbędnych do połączenia z bazą danych
    def show_setup_window(self):
        SetupWindow()

