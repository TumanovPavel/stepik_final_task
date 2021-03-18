from selenium import webdriver
import time
import math
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket") != None, \
        "Кнока 'Добавить в корзину' не найдена на странице"