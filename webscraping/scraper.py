from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class WebScraper:
    def __init__(self) -> None:
        self.url = "https://asloterias.com.br/resultados-da-mega-sena-2022"
        # self.url = "https://asloterias.com.br/todos-resultados-mega-sena"
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
        self.driver.get(self.url)
        sleep(5)
        counter = 1
        for i in range(110):
            print(self.driver.find_element(By.XPATH, self.map['raffle']['xpath'].replace('#counter#', str(i+4))).text, end=": ")
            for j in range(6):
                print(self.driver.find_element(By.XPATH, self.map['number']['xpath'].replace('#sec_counter#', str(counter))).text, end=" ")
                counter += 1
            print()
