from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Item in the basket is presented, but should not be"

    def check_empty_basket_text(self):
        empty_text = self.browser.find_element(*BasketPageLocators.EMPTY_TEXT).text
        assert "Your basket is empty." in empty_text, "Empty text is not presented"