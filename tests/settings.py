import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBLOCATION = BASE_DIR + '/tests/lib'
BROWSERTYPE = 'CHROME'  # Select from ['CHROME', 'FIREFOX', 'SAFARI']
BROWSEROS = 'OSX'  # Select from ['OSX', 'WINDOWS', 'LINUX']

WDW_TIME = 4
URL = 'https://www.amazon.com/'
