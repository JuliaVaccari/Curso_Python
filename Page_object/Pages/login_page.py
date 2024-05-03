from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class Preencher_Login(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def preencher_login(self, username, password):
        self.wait_for_element(self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        sleep(1)
        self.driver.find_element(*self.LOGIN).click()