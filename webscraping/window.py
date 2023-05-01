import tkinter as tk
from tkinter import ttk

from mega_years import MEGA_YEARS
window = tk.Tk()


class Application():
    def __init__(self) -> None:
        self.MEGA_YEARS = MEGA_YEARS
        self.window = window
        self.screen()
        self.frame()
        self.inputs()
        self.list_megas()
        self.dropdown()
        window.mainloop()

    def screen(self):
        self.window.title("Mega-Sena")
        self.window.geometry('900x650')
        self.window.configure(background='#27a15b', border=0.8)
        self.window.resizable(False, False)

    def frame(self):
        self.frame_0 = tk.Frame(self.window, bg="#5effa4")
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.09)

        self.frame_1 = tk.Frame(self.window, bg='#5effa4')
        self.frame_1.place(relx=0.03, rely=0.14, relwidth=0.94, relheight=0.4)

        self.frame_2 = tk.Frame(self.window, bg='#5effa4')
        self.frame_2.place(relx=0.03, rely=0.56, relwidth=0.94, relheight=0.4)

    def inputs(self):
        self.input_n1 = tk.Entry(self.frame_0, border=0, font=("sans-serif", 16))
        self.input_n1.place(relx=0.01, rely=0.20, relwidth=0.05, relheight=0.7)

        self.input_n2 = tk.Entry(self.frame_0, border=0, font=("sans-serif", 16))
        self.input_n2.place(relx=0.08, rely=0.20, relwidth=0.05, relheight=0.7)

        self.input_n3 = tk.Entry(self.frame_0, border=0, font=("sans-serif", 16))
        self.input_n3.place(relx=0.15, rely=0.20, relwidth=0.05, relheight=0.7)

        self.input_n4 = tk.Entry(self.frame_0, border=0, font=("sans-serif", 16))
        self.input_n4.place(relx=0.22, rely=0.20, relwidth=0.05, relheight=0.7)

        self.input_n5 = tk.Entry(self.frame_0, border=0, font=("sans-serif", 16))
        self.input_n5.place(relx=0.29, rely=0.20, relwidth=0.05, relheight=0.7)

        self.input_n6 = tk.Entry(self.frame_0, border=0, font=("sans-serif", 16))
        self.input_n6.place(relx=0.36, rely=0.20, relwidth=0.05, relheight=0.7)

    def dropdown(self):
        variable = tk.StringVar(self.window)
        variable.set(self.MEGA_YEARS[0])

        dropdown = tk.OptionMenu(self.frame_0, variable, *self.MEGA_YEARS)
        dropdown.pack()
        dropdown.place(relx=0.88, rely=0.20, relwidth=0.1, relheight=0.7)

    def list_megas(self):
        self.list_megas_tb = ttk.Treeview(
            self.frame_1,
            height=3,
            columns=(
                'col0', 'col1', 'col2', 'col3'
                )
            )
        self.list_megas_tb.heading('#0', text='')
        self.list_megas_tb.heading('#1', text='CONTEST')
        self.list_megas_tb.heading('#2', text='NUMBERS')
        self.list_megas_tb.heading('#3', text='DATE')

        self.list_megas_tb.column('#0', width=0)
        self.list_megas_tb.column('#1', width=100)
        self.list_megas_tb.column('#2', width=300)
        self.list_megas_tb.column('#3', width=250)

        self.list_megas_tb.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)
        self.scrool_list = tk.Scrollbar(self.frame_1, orient='vertical')
        self.list_megas_tb.configure(yscrollcommand=self.scrool_list.set)
        self.scrool_list.place(relx=0.97, rely=0.02, relwidth=0.03, relheight=0.96)


windowapp = Application()
