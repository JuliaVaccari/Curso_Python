import pytest
from selenium import webdriver
from Pages.base_page import BasePage
from Pages.login_page import Preencher_Login
from Pages.products_page import Add_to_cart
from Pages.your_cart_page import Your_cart
from Pages.checkout_your_inf_page import Register
from Pages.checkout_overview_page import Finish
from Pages.checkout_complete_page import Complete_order
from Config.webdriver_singleton import WebDriverSingleton
from time import sleep

@pytest.fixture()
def driver():
    driver = WebDriverSingleton.get_instance()
    BasePage(driver).go_to_site()
    yield driver

@pytest.fixture(scope="session", autouse=True)
def close_browser():
    yield
    WebDriverSingleton.quit_instance()

def atest_first_order(driver):
    login = Preencher_Login(driver)
    login.preencher_login("standard_user", "secret_sauce")

    products_page = Add_to_cart(driver)
    products = products_page.get_all_products_buttons()

    for product in products:
        product.click()
   
    bagde = products_page.get_bagde()
    assert  bagde == "6"
    sleep(1)

    products_page.click_cart()

    Remove_item_1= Your_cart(driver)
    Remove_item_1.remove_bolt_tshirt()

    bagde = products_page.get_bagde()
    assert  bagde == "5"
    sleep(1)

    checkout = Your_cart(driver)
    checkout.checkout_button()

    your_information = Register(driver)
    your_information.register("Julia", "Vaccari", "123456")

    button_finish = Finish(driver)
    button_finish.button_finish()

    complete_order = Complete_order(driver)
    messege = complete_order.messege()
    assert messege == "Thank you for your order!"

def atest_second_order(driver):
    
    login = Preencher_Login(driver)
    login.preencher_login("standard_user", "secret_sauce")

    products_page = Add_to_cart(driver)
    products_page.button_add_backpack()
    products_page.button_add_bike_light()

    sleep(2)

    bagde = products_page.get_bagde()
    assert  bagde == "2"

    products_page.click_cart()

    your_cart = Your_cart(driver)
    your_cart.button_continue_shopping()

    products_page.button_add_tshirt()

    bagde = products_page.get_bagde()
    assert  bagde == "3"

    products_page.click_cart()

    checkout = Your_cart(driver)
    checkout.checkout_button()

    your_information = Register(driver)
    your_information.register("Julia", "Vaccari", "123456")

    button_finish = Finish(driver)
    button_finish.button_finish()

    complete_order = Complete_order(driver)
    messege = complete_order.messege()
    assert messege == "Thank you for your order!"

def atest_checkout(driver):

    login = Preencher_Login(driver)
    login.preencher_login("standard_user", "secret_sauce")

    products_page = Add_to_cart(driver)
    products_page.button_add_backpack()
    products_page.button_add_bike_light()

    sleep(2)

    bagde = products_page.get_bagde()
    assert  bagde == "2"

    products_page.click_cart()

    checkout = Your_cart(driver)
    checkout.checkout_button()

    your_information = Register(driver)
    your_information.register("Julia", "Vaccari", "")

    sleep(2)

    error_checkout = Register(driver)
    messege_error_checkout = error_checkout.fail_register()

    assert  messege_error_checkout == "Error: Postal Code is required"

    your_information.register("Julia", "Vaccari", "123456")

    button_finish = Finish(driver)
    button_finish.button_finish()

    complete_order = Complete_order(driver)
    messege = complete_order.messege()
    assert messege == "Thank you for your order!"

def test_empty_cart(driver):

    login = Preencher_Login(driver)
    login.preencher_login("standard_user", "secret_sauce")

    products_page = Add_to_cart(driver)
    products_page.button_add_backpack()
    products_page.button_add_bike_light()

    sleep(2)

    bagde = products_page.get_bagde()
    assert  bagde == "2"

    products_page.click_cart()

    checkout = Your_cart(driver)
    checkout.checkout_button()

    your_information = Register(driver)
    your_information.register("Julia", "Vaccari", "123456")

    buttun_cancel = Finish(driver)
    buttun_cancel.button_cancel()

    products_page.button_rem_backpack()
    products_page.button_rem_bike_light()

    products_page.click_cart()

    checkout = Your_cart(driver)
    checkout.checkout_button()

    your_information = Register(driver)
    your_information.register("Julia", "Vaccari", "123456")

    empty_cart = Finish(driver)
    total_price = empty_cart.price_total_total()
    assert total_price == "Total: $0.00"

