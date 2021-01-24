from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button")
    MESSAGE_FORM = (By.CSS_SELECTOR, "#messages")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, "#messages div.alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#success_messages")

