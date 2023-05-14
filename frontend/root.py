import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("920x720")
        self.title("Çelebi Seyahat Acentası")
        self.configure(bg="cyan")
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=5)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=99)
        self.grid_propagate(False)