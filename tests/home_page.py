from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from tests.selenium_page import BasePage


class Home(BasePage):
    class LOCATORS(object):
        SEARCH = (By.ID, 'twotabsearchtextbox')
        BEST_SELLER = (By.XPATH, ".//span[@class='a-badge-label-inner a-text-ellipsis'] /span[text()='Best Seller']")
        RESULT_ITEMS = (By.CSS_SELECTOR, '.a-section.a-spacing-medium')
        RESULT_ROWS = '.sg-row'
        LINK = '.a-link-normal'

    def enter_text_and_press_enter(self, text):
        self.fill_element(self.LOCATORS.SEARCH, text)
        self.press_enter(self.LOCATORS.SEARCH)

    def result_items(self):
        return self.find_all_elements(self.LOCATORS.RESULT_ITEMS)

    def get_best_sellers(self):
        # We don't know how many best sellers will be in the result.
        # To look elements by text won't work in this case because after we find them we need to click on them.
        # Let's find a parent element of rows and then loop through them to check if they are best sellers.
        best_sellers_links = set()
        all_items = self.result_items()
        for result in all_items:
            rows = result.find_elements(By.CSS_SELECTOR, self.LOCATORS.RESULT_ROWS)
            for index, row in enumerate(rows):
                try:
                    get_href = row.find_element(By.CSS_SELECTOR,
                                                '.a-section.a-spacing-micro.s-min-height-small ' + self.LOCATORS.LINK)
                except NoSuchElementException:
                    # some elements don't have a link. So we expect this exception
                    continue

                if 'bestsellers' not in get_href.get_attribute('href'):
                    continue

                # next row element has a direct link for the best seller
                next_row = rows[index + 1].find_element(By.CSS_SELECTOR, self.LOCATORS.LINK)
                best_sellers_links.add(next_row.get_attribute('href'))
        return list(best_sellers_links)
