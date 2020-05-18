import tkinter as tk
from tkinter import *


class SetupWindow():

    def __init__(self):
        master = tk.Tk()
        master.title("Setup database connection")
        master.resizable(False, False)
        window_height = 220
        window_width = 295
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        tk.Label(master, text="Adress").grid(row=0, sticky=W, padx=10, pady=5)
        tk.Entry(master, bd=1).grid(row=0, column=1, padx=20, pady=5)

        tk.Label(master, text="Port").grid(row=1, sticky=W, padx=10, pady=5)
        tk.Entry(master, bd=1).grid(row=1, column=1, padx=20, pady=5)

        tk.Label(master, text="Data base user").grid(row=2, sticky=W, padx=10, pady=5)
        tk.Entry(master, bd=1).grid(row=2, column=1, padx=20, pady=5)

        tk.Label(master, text="Data base name").grid(row=3, sticky=W, padx=10, pady=5)
        tk.Entry(master, bd=1).grid(row=3, column=1, padx=20, pady=5)

        connection_info = tk.Label(master).grid(row=4, sticky=W, padx=20, pady=5)

        button1 = tk.Button(master, text='Test connetion', height=2, width=15).grid(row=5, column=0, padx=10, pady=5)
        button2 = tk.Button(master, text='Save', height=2, width=15).grid(row=5, column=1, padx=10, pady=5)

        master.mainloop()

    def __del__(self):
        return