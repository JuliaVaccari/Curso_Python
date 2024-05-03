from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class Your_cart (BasePage):
    REMOVE_TSHIRT = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    BUTTON_CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def remove_bolt_tshirt (self):
        self.wait_for_element(self.REMOVE_TSHIRT).click()

    def checkout_button (self):
        self.wait_for_element(self.CHECKOUT_BUTTON).click()

    def button_continue_shopping (self):
        self.driver.find_element(*self.BUTTON_CONTINUE_SHOPPING).click()

