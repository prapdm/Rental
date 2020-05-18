import tkinter as tk
from tkinter import messagebox


class MainWindow():
    def __init__(self):
        self.master = tk.Tk()
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title( "Rental 1.0" )
        self.button1 = tk.Button(self.frame, text = 'New User', height = 2, width = 20, command = self.new_window)
        self.button1.pack(padx=90, pady=10)

        self.frame.pack()
        self.master.mainloop()

    def new_window(self):
        self.UserWindow = tk.Toplevel(self.master)
        self.app = NewUserWindow(self.UserWindow)


    def confirmexit(self):
        answer = messagebox.askquestion("Title", "Are you sure you want to leave?")
        if answer == "yes":
            self.master.destroy()
