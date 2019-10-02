import pytest
from tests.selenium_utils import start_driver


@pytest.fixture(scope='function')
def _driver():
    driver = start_driver()
    yield driver
    driver.quit()


@pytest.fixture
def driver(_driver):
    yield _driver
    _driver.delete_all_cookies()
