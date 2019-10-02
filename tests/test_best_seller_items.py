from tests.settings import URL
from tests import home_page
from tests import product_details_page


def test_add_best_sellers(driver):
    driver.get(URL)
    page = home_page.Home(driver)
    assert driver.current_url == URL

    page.enter_text_and_press_enter('Headphones')
    best_seller_links = page.get_best_sellers()
    product_page = product_details_page.DetailsPage(driver)

    for count, link in enumerate(best_seller_links):
        driver.get(link)
        product_page.add_to_cart()
        assert product_page.get_cart_amount(expected=str(count + 1)) is True
        assert product_page.item_added() is True