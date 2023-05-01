from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from mega_years import MEGA_YEARS
from db_functions import insert_db, create_table


class WebScraper:
    def __init__(self) -> None:
        self.url = "https://asloterias.com.br/resultados-da-mega-sena-#YEAR#"
        self.map = {
            "raffle": {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[#counter#]'
            },
            "number": {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/span[#sec_counter#]'
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_site(self):
        for year in MEGA_YEARS:
            # year = '2014'
            self.driver.get(self.url.replace('#YEAR#', year))
            sleep(5)
            print("========== YEAR:", year, "==========")
            self.get_numbers(year)

    def get_numbers(self, year):
        create_table(year)
        table = f"mega{year}"
        counter = 1
        i = 0
        while True:
            numbers = []
            try:
                contest = self.driver.find_element(By.XPATH, self.map['raffle']['xpath'].replace('#counter#', str(i+4))).text
                print(contest, end=": ")
                j = 0
                while j < 6:
                    number = self.driver.find_element(By.XPATH, self.map['number']['xpath'].replace('#sec_counter#', str(counter))).text
                    print(number, end=" ")
                    counter += 1
                    if number != "Mega da Virada":
                        numbers.append(number)
                        j += 1
                i += 1
                insert_db(table=table, year=year, contest=contest, numbers=numbers)
                print()
            except Exception as e:
                print(e)
                break
