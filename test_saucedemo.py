import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    yield driver
    driver.quit()

def test_first_order(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(1)

    logo = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert logo == "Swag Labs"

    products=driver.find_elements(By.XPATH, '//button[contains(@data-test, "add-to-cart")]')

    for product in products:
        sleep(1)
        product.click()

    # item1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    # item1.click()

    # item2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    # item2.click()

    # item3 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    # item3.click()

    # item4 = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    # item4.click()

    # item5 = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    # item5.click()

    # item6 = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    # item6.click()

    sleep(2)

    bagde = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert bagde=="6"
    
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    remove1 = driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt")
    remove1.click()

    sleep(3)

    bagde = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert bagde=="5"

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    sleep(1)

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Julia")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Vaccari")

    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("123456")

    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()

    sleep(1)

    button_finish = driver.find_element(By.ID, "finish")
    button_finish.click()

    sleep(1)

    messege = driver.find_element(By.CLASS_NAME, "complete-header").text

    assert messege=="Thank you for your order!"

#Caso 02:
# - Logar no site com o usuário standard
# - Adicionar 2 produtos no carrinho
# - Conferir que no carrinho tem a badge com 2 produtos
# - Ir para o carrinho de compras
# - Clicar no botão continue shopping
# - Adicionar mais 1 produto
# - Conferir que no carrinho tem a badge com 3 produtos
# - Ir para o carrinho de compras
# - Clicar no botão Checkout
# - ○ Preencher os dados solicitados e clicar em Continue
# - ○ Clicar no botão Finish
# - ○ Conferir a mensagem “Thank you for your order!”
    
def test_second_order(driver):
    username = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username.send_keys("standard_user")

    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys("secret_sauce")

    login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login.click()

    sleep(1)

    item1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    item1.click()

    item2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    item2.click()

    sleep(2)

    bagde = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert bagde=="2"
    
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    button_continue_shopping = driver.find_element(By.ID, "continue-shopping")
    button_continue_shopping.click()

    item3 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    item3.click()

    bagde = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert bagde=="3"
    
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    sleep(1)

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Julia")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Vaccari")

    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("123456")

    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()

    sleep(1)

    button_finish = driver.find_element(By.ID, "finish")
    button_finish.click()

    sleep(1)

    messege = driver.find_element(By.CLASS_NAME, "complete-header").text

    assert messege=="Thank you for your order!"

#Caso 03:

# - Logar no site com o usuário standard
# - Adicionar 2 produtos no carrinho
# - Conferir que no carrinho tem a badge com 2 produtos
# - Ir para o carrinho de compras
# - Clicar no botão Checkout
# - Preencher name
# - Não preencher last name 
# - Preencher zip code
# - Confirmar mensagem de erro 
# - Preencher novamente os dados do checkout corretamente e clicar em continue 
# - ○ Clicar no botão Finish
# - ○ Conferir a mensagem “Thank you for your order!”

def test_checkout(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(1)

    logo = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert logo == "Swag Labs"

    item1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    item1.click()

    item2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    item2.click()

    sleep(2)

    bagde = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert bagde=="2"
    
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    sleep(1)

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Julia")

    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("123456")

    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()

    error_checkout = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
    assert error_checkout=="Error: Last Name is required"

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Julia")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Vaccari")

    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("123456")

    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()

    sleep(1)

    button_finish = driver.find_element(By.ID, "finish")
    button_finish.click()

    sleep(1)

    messege = driver.find_element(By.CLASS_NAME, "complete-header").text

    assert messege=="Thank you for your order!"

#Caso 04

# - Logar no site com o usuário standard
# - Adicionar 2 produtos no carrinho
# - Conferir que no carrinho tem a badge com 2 produtos
# - Ir para o carrinho de compras
# - Clicar no botão Checkout
# - Preencher os dados solicitados e clicar em Continue
# - Clicar no botão cancel
# - Remover os dois produtos do carrinho
# - Clicar no carrinho 
# - Clicar no botão Checkout 
# - Preencher os dados solicitados e clicar em Continue
# - Verificar o valor do carrinho igual a 0
    
def test_empty_cart(driver):

    username = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username.send_keys("standard_user")

    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys("secret_sauce")

    login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login.click()

    sleep(1)

    item1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    item1.click()

    item2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    item2.click()

    sleep(2)

    bagde = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert bagde=="2"
    
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    sleep(1)

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Julia")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Vaccari")

    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("123456")

    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()

    button_cancel = driver.find_element(By.XPATH, '//button[@id="cancel"]')
    button_cancel.click()

    remove_item1 = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    remove_item1.click()

    remove_item2 = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-bike-light"]')
    remove_item2.click()

    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    sleep(1)

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Julia")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Vaccari")

    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("123456")

    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()

    empty_cart = driver.find_element(By.XPATH, '//div[@class="summary_info_label summary_total_label"]').text
    assert empty_cart == "Total: $0.00"

#Caso 05

# - Logar no site com o usuário standard
# - Ordenar por menor preço
# - Conferir se os preços foram ordenados corretamente

def test_sorted_prices(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login = driver.find_element(By.ID, "login-button")
    login.click()

    sleep(1)

    logo = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert logo == "Swag Labs" 

    Select(driver.find_element(By.CLASS_NAME,"product_sort_container")).select_by_visible_text("Price (low to high)")

    sleep(5)

    produts=driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    prices = []

    for product in produts:
        price=product.text
        price=price.replace("$","")
        prices.append(float(price))

    sorted_price = sorted(prices)

    assert sorted_price == prices