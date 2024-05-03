from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class Register (BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.ID, "continue")
    ERROR_CHECKOUT = (By.XPATH, "//h3[@data-test='error'][contains(.,'Error: Postal Code is required')]")

    def register (self, first_name, last_name, zip_code):
        self.wait_for_element(self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)
        self.driver.find_element(*self.BUTTON_CONTINUE).click()
        sleep(1)

    def fail_register (self):
        return self.driver.find_element(*self.ERROR_CHECKOUT).text