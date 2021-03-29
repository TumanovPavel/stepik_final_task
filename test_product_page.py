from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import faker

LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
OFFER_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        f = faker.Faker()
        email = f.email()
        password = f.password()
        login_page.register_new_user(email,password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.product_name_in_the_message_compare_the_added_product()
        product_page.product_price_in_the_basket_compare_the_added_product()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, OFFER_LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()
    basket_page.check_empty_basket_text()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    page = ProductPage(browser, OFFER_LINK )
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, OFFER_LINK )
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_success_message()

@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                 pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_name_in_the_message_compare_the_added_product()
    product_page.product_price_in_the_basket_compare_the_added_product()