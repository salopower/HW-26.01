import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class', autouse=True)
def get_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-extensions")
    driver = Chrome(ChromeDriverManager().install(), options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def refresh_page(request):
    driver = request.getfixturevalue("get_chrome")
    yield
    driver.refresh()
