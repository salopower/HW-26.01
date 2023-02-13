import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome(executable_path='C:\DRIVERS\chromedriver_win32\chromedriver.exe')


@pytest.fixture
def dynamic_properties():
    driver.get('https://demoqa.com/dynamic-properties')


@pytest.fixture()
def get_elem_id():
    elem = driver.find_element(By.XPATH, '//p[text()="This text has random Id"]')
    yield elem.get_attribute('id')


def test_random_elem_text(get_elem_id):
    random_text_elem = driver.find_element(By.ID, get_elem_id)
    assert 'random' in random_text_elem.text


def test_wait_for_enable_element():
    enable_button = driver.find_element(By.CSS_SELECTOR, '#enableAfter')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable(enable_button))
    assert enable_button.is_enabled()


def test_button_is_present():
    visible_button = driver.find_element(By.CSS_SELECTOR, '#visibleAfter')
    assert not visible_button.is_displayed()
    driver.refresh()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of(visible_button))
    assert visible_button.is_displayed()
