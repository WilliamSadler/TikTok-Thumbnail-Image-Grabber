from tkinter import *
try:
    import Tkinter as tk
except:
    import tkinter as tk

import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk

WINDOW_TITLE = "HELP ME I AM BEING HELD HOSTAGE"

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)  
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title(WINDOW_TITLE)

        # allowing the widget to take the full space of the root window
        self.grid(column=0, row=0)

class ThumbnailGeneratorGUI:
    def __init__(self):
        self.initialise_root()

    def initialise_root(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.resizable(False, False)

    def open_gui(self):
        app = Window(self.root)
        self.root.mainloop()
        