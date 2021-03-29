from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class BasketPageLocators():
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket-items")

class ProductPageLocators():
    ADD_BASKET_BUTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_THE_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    PRODUCT_NAME_IN_THE_CATALOG = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE_IN_THE_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')
    PRODUCT_PRICE_IN_THE_CATALOG = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
