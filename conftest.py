import pytest
from selene.support.shared import config, browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class', name='demoqa', autouse=False)
def set_browser_for_demoqa():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--start-maximized')
    config.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    config.base_url = 'https://demoqa.com/'
    yield
    browser.quit()
