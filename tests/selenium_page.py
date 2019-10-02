from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.settings import WDW_TIME


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_by_locator(self, locator, wait=WDW_TIME):
        while self.driver.execute_script('return document.readyState') == 'complete':
            return WebDriverWait(self.driver, wait, ignored_exceptions=[StaleElementReferenceException]). \
                until(EC.presence_of_element_located(locator))

    def find_by_locator_and_clickability(self, locator, wait=WDW_TIME):
        while self.driver.execute_script('return document.readyState') == 'complete':
            return WebDriverWait(self.driver, wait, ignored_exceptions=[StaleElementReferenceException]). \
                until(EC.element_to_be_clickable(locator))

    def find_all_elements(self, locator, wait=WDW_TIME):
        items = WebDriverWait(self.driver, wait,
                              ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException]). \
            until(EC.presence_of_all_elements_located(locator))
        return items

    def fill_element(self, locator, value):
        element = self.find_by_locator(locator)
        element.send_keys(value)

    def press_enter(self, locator):
        element = self.find_by_locator(locator)
        element.send_keys(Keys.ENTER)



