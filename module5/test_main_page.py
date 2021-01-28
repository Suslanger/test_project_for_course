from .pages.main_page import MainPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/#"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_products()
    page.should_be_message_empty_basket()