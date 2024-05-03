from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class Finish (BasePage):
    BUTTON_FINISH = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    EMPTY_CART = (By.XPATH, '//div[@class="summary_total_label"]')

    def button_finish(self):
        self.wait_for_element(self.BUTTON_FINISH).click()

    def button_cancel(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()

    def price_total_total(self):
        return self.driver.find_element(*self.EMPTY_CART).text
