# -*- coding: utf-8 -*-
import tkinter as tk
from NewUserWindow import NewUserWindow
from tkinter import messagebox


class MainWindow:
    def __init__(self, cnx):
        self.cnx = cnx
        self.master = tk.Tk()
        self.frame = tk.Frame(self.master)
        self.master.title("Rental 1.0")
        self.button1 = tk.Button(self.frame, text='New User', height=2, width=20, command=self.new_window)
        self.button1.pack(padx=90, pady=10)
        self.button2 = tk.Button(self.frame, text='Find User', height=2, width=20, command=self.new_window)
        self.button2.pack(padx=90, pady=10)
        self.button3 = tk.Button(self.frame, text='User List', height=2, width=20, command=self.new_window)
        self.button3.pack(padx=90, pady=10)
        self.button4 = tk.Button(self.frame, text='New Position', height=2, width=20, command=self.new_window)
        self.button4.pack(padx=90, pady=10)
        self.button5 = tk.Button(self.frame, text='Find Position', height=2, width=20, command=self.new_window)
        self.button5.pack(padx=90, pady=10)
        self.button6 = tk.Button(self.frame, text='Exit', height=2, width=20, command=self.confirmexit)
        self.button6.pack(padx=90, pady=10)

        self.frame.pack()
        self.master.mainloop()

    def new_window(self):
        self.UserWindow = tk.Toplevel(self.master)
        self.app = NewUserWindow(self.UserWindow, self.cnx)

    def confirmexit(self):
        answer = messagebox.askquestion("Title", "Are you sure you want to leave?")
        if answer == "yes":
            self.master.destroy()
