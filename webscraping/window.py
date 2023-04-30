import tkinter as tk
from tkinter import ttk

window = tk.Tk()


class Application():
    def __init__(self) -> None:
        self.window = window
        self.screen()
        self.frame()
        self.inputs()
        window.mainloop()

    def screen(self):
        self.window.title("Mega-Sena")
        self.window.geometry('900x650')
        self.window.configure(background='#27a15b', border=0.8)
        self.window.resizable(False, False)

    def frame(self):
        self.frame_0 = tk.Frame(self.window, bg="#ffffff")
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.09)

    def inputs(self):
        ...


windowapp = Application()
