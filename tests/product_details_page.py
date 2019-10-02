from selenium.webdriver.common.by import By

from tests.selenium_page import BasePage


class DetailsPage(BasePage):
    class LOCATORS(object):
        ADD_TO_CART = (By.ID, 'add-to-cart-button')
        CART_COUNT = (By.ID, 'nav-cart-count')
        CLOSE_ICON_MODAL = (By.CSS_SELECTOR, '.a-popover.a-popover-modal.a-declarative .a-icon.a-icon-close')
        ITEM_ADDED = (By.ID, 'huc-v2-order-row-confirm-text')
        ATTACH_PANE_NO_THANKS = (By.ID, 'attachSiNoCoverage-announce')
        ATTACH_ADDED = (By.ID, 'attachDisplayAddBaseAlert')

    def add_to_cart(self):
        return self.find_by_locator(self.LOCATORS.ADD_TO_CART).click()

    def close_modal(self):
        self.find_by_locator(self.LOCATORS.CLOSE_ICON_MODAL).click()

    def close_panel(self):
        self.find_by_locator(self.LOCATORS.ATTACH_PANE_NO_THANKS).click()

    def get_cart_amount(self, expected, tries=10):
        for i in range(tries):
            el = self.find_by_locator(self.LOCATORS.CART_COUNT)
            if el.text == expected:
                return True

            # the modal and the panel on the right appear randomly while shopping.
            # they block user to add items. Let's try to close it
            try:
                self.close_modal()
            except:
                try:
                    self.close_panel()
                except:
                    continue

    def item_added(self):
        # we don't know how the item was added so we need to handle 2 cases to verify the text
        try:
            el = self.find_by_locator(self.LOCATORS.ITEM_ADDED)
        except:
            try:
                el = self.find_by_locator(self.LOCATORS.ATTACH_ADDED)
            except:
                pass
        if el.text == 'Added to Cart':
            return True


