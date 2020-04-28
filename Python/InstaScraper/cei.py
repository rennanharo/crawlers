from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from secrets import cpf, pwcei

class CeiBot:
    def __init__(self, cpf, pw):
        self.cpf = cpf
        self.pw = pw

        self.driver = webdriver.Chrome()
        self.driver.get("https://cei.b3.com.br")
        sleep(2)

        self.driver.find_element_by_xpath("/html/body/form/div[8]/div/div/div/div[1]/div/div[1]/div[1]/input").send_keys(cpf)
        self.driver.find_element_by_xpath("/html/body/form/div[8]/div/div/div/div[2]/div/div[1]/div[1]/input").send_keys(pw)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/form/div[8]/div/div/div/div[3]/div/div/input").click()
        sleep(10)

    def getStocks(self):
        self.driver.get("https://cei.b3.com.br/CEI_Responsivo/ConsultarCarteiraAtivos.aspx")
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/form/div[7]/div[2]/div/input").click()
        sleep(60)


CeiBot(cpf, pwcei).getStocks()