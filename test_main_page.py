from selenium import webdriver
import time
import math
import pytest

def test_add_to_basket_button_is_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket") != None, \
        "Кнока 'Добавить в корзину' не найдена на странице"