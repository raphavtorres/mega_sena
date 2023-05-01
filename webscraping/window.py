import tkinter as tk
from tkinter import ttk

from mega_years import MEGA_YEARS
from db_functions import read_game_db
from scraper import WebScraper

window = tk.Tk()


class Application():
    def __init__(self) -> None:
        self.MEGA_YEARS = MEGA_YEARS
        self.window = window
        self.screen()
        self.frame()
        self.buttons()
        self.inputs()
        self.list_megas()
        self.comboBox()
        # self.dropdown()
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

    def buttons(self):
        self.btn_search = tk.Button(self.frame_0, bg="#7a2c64", border=0, text="Search", font=("sans-serif", 12), fg="#ffffff", command=self.read_game)
        self.btn_search.place(relx=0.77, rely=0.20, relwidth=0.1, relheight=0.7)

        self.btn_update = tk.Button(self.frame_0, bg="#7a2c64", border=0, text="Update", font=("sans-serif", 12), fg="#ffffff", command=self.update)
        self.btn_update.place(relx=0.6, rely=0.20, relwidth=0.1, relheight=0.7)

        self.btn_fezinha = tk.Button(self.frame_0, bg="#7a2c64", border=0, text="Fezinha", font=("sans-serif", 12), fg="#ffffff")
        self.btn_fezinha.place(relx=0.42, rely=0.20, relwidth=0.1, relheight=0.7)

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

    def comboBox(self):
        self.cb_years = ttk.Combobox(self.frame_0, values=MEGA_YEARS, font=("sans-serif", 12))
        self.cb_years.set(self.MEGA_YEARS[0])
        self.cb_years.pack()
        self.cb_years.place(relx=0.88, rely=0.20, relwidth=0.1, relheight=0.7)

    def list_megas(self):
        self.list_megas_tb = ttk.Treeview(
            self.frame_1,
            height=3,
            columns=(
                'col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'
                )
            )
        self.list_megas_tb.heading('#0', text='')
        self.list_megas_tb.heading('#1', text='YEAR')
        self.list_megas_tb.heading('#2', text='CONTEST')
        self.list_megas_tb.heading('#3', text='N1')
        self.list_megas_tb.heading('#4', text='N2')
        self.list_megas_tb.heading('#5', text='N3')
        self.list_megas_tb.heading('#6', text='N4')
        self.list_megas_tb.heading('#7', text='N5')
        self.list_megas_tb.heading('#8', text='N6')
        self.list_megas_tb.heading('#9', text='DATE')

        self.list_megas_tb.column('#0', width=0)
        self.list_megas_tb.column('#1', width=80)
        self.list_megas_tb.column('#2', width=80)
        self.list_megas_tb.column('#3', width=80)
        self.list_megas_tb.column('#4', width=80)
        self.list_megas_tb.column('#5', width=80)
        self.list_megas_tb.column('#6', width=80)
        self.list_megas_tb.column('#7', width=80)
        self.list_megas_tb.column('#8', width=80)
        self.list_megas_tb.column('#9', width=100)

        self.list_megas_tb.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)
        self.scrool_list = tk.Scrollbar(self.frame_1, orient='vertical')
        self.list_megas_tb.configure(yscrollcommand=self.scrool_list.set)
        self.scrool_list.place(relx=0.97, rely=0.02, relwidth=0.03, relheight=0.96)

    def read_game(self):
        self.clear()
        year = self.get_year()
        table = f'mega{year}'
        games = read_game_db(table)
        for game in games:
            self.list_megas_tb.insert("", "end", values=game)

    def clear(self):
        self.list_megas_tb.delete(*self.list_megas_tb.get_children())
        self.input_n1.delete(0, tk.END)
        self.input_n2.delete(0, tk.END)
        self.input_n3.delete(0, tk.END)
        self.input_n4.delete(0, tk.END)
        self.input_n5.delete(0, tk.END)
        self.input_n6.delete(0, tk.END)

    def get_year(self):
        year = self.cb_years.get()
        return year

    def update(self):
        year = self.get_year()
        web_scraper_update = WebScraper()
        web_scraper_update.open_site(year)


windowapp = Application()
