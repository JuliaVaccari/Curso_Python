from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class Complete_order (BasePage):
    MESSEGE = (By.CLASS_NAME, "complete-header")

    def messege (self):
        return self.wait_for_element(self.MESSEGE).text