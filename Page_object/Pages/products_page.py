from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class Add_to_cart (BasePage):
    PRODUCTS = (By.XPATH, "//button[contains(@data-test, 'add-to-cart')]")   
    BAGDE =  (By.XPATH, "//span[@class='shopping_cart_badge']")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    ADD_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    REM_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REM_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")

    def get_all_products_buttons(self):
        self.wait_for_element(self.PRODUCTS)
        return self.driver.find_elements(*self.PRODUCTS)
        
    def get_bagde(self):
        return self.driver.find_element(*self.BAGDE).text
        
    def click_cart(self):
        self.driver.find_element(*self.CART).click()

    def button_add_backpack(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def button_add_bike_light(self):
        self.driver.find_element(*self.ADD_BIKE_LIGHT).click()

    def button_add_tshirt(self):
        self.driver.find_element(*self.ADD_TSHIRT).click()

    def button_rem_backpack(self):
        self.driver.find_element(*self.REM_BACKPACK).click()

    def button_rem_bike_light(self):
        self.driver.find_element(*self.REM_BIKE_LIGHT).click()
    