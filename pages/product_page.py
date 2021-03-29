from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_basket_buton = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTON)
        add_basket_buton.click()

    def product_name_in_the_message_compare_the_added_product(self):
        product_name_in_the_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_THE_MESSAGE).text
        product_name_in_the_catalog = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_THE_CATALOG).text
        assert product_name_in_the_message == product_name_in_the_catalog, 'The name of the product in the message ' \
                                                                           'does not match the added product '

    def product_price_in_the_basket_compare_the_added_product(self):
        product_price_in_the_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_THE_MESSAGE).text
        product_price_in_the_catalog = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_THE_CATALOG).text
        assert product_price_in_the_message == product_price_in_the_catalog, 'The price of the product in the message ' \
                                                                             'does not match the added product '

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
