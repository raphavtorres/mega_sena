from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# from mega_years import MEGA_YEARS
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
            },
            "date": {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/text()[#third_counter]'
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    """
    /html/body/main/div[2]/div/div/div[1]/text()[8]
    /html/body/main/div[2]/div/div/div[1]/text()[10]
    """

    def open_site(self, year=""):
        # for year in MEGA_YEARS:
        # year = '2022'
        self.driver.get(self.url.replace('#YEAR#', year))
        sleep(5)
        print("========== YEAR:", year, "==========")
        self.get_numbers(year)

    def get_numbers(self, year):
        create_table(year)
        table = f"mega{year}"
        counter = 1
        third_counter = 8
        i = 0
        while True:
            numbers = []
            try:
                contest = self.driver.find_element(By.XPATH, self.map['raffle']['xpath'].replace('#counter#', str(i+4))).text
                # date = self.driver.find_element(By.XPATH, self.map['date']['xpath'].replace('#third_counter', str(third_counter))).get_attribute("outerHTML")
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
                third_counter += 2
                # print(date)
                insert_db(table=table, year=year, contest=contest, numbers=numbers)
                print()
            except Exception as e:
                print(e)
                break
