from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from tests.settings import BROWSERTYPE, BROWSEROS, LIBLOCATION


# Creates an instance of the webdriver based on the config file
def start_driver():
    if BROWSERTYPE == 'CHROME' and \
            (BROWSEROS == 'OSX' or BROWSEROS == 'LINUX' or BROWSEROS == 'WINDOWS'):
        if BROWSEROS == 'WINDOWS':
            CHROMEDRIVER_LOCATION = LIBLOCATION + '/chromedriver.exe'
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ['test-type'])
            loggingPrefs = \
                {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL', 'performance': 'ALL', 'server': 'ALL'}

            CHROMEDRIVER_LOCATION = LIBLOCATION + '/chromedriver'
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = loggingPrefs
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_LOCATION, chrome_options=options,
                                  desired_capabilities=d)
    elif BROWSEROS == 'OSX' and BROWSERTYPE == 'SAFARI':
        driver = webdriver.Safari()
    elif BROWSERTYPE == 'FIREFOX':
        GECKODRIVER_LOCATION = LIBLOCATION + '/geckodriver'
        firefox_capabilities = DesiredCapabilities.FIREFOX
        driver = webdriver.Firefox \
            (capabilities=firefox_capabilities, executable_path=GECKODRIVER_LOCATION)
    else:
        pass

    driver.set_window_size(1920, 1080)
    return driver
