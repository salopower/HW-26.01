import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def dynamic_properties(request):
    driver = request.getfixturevalue("get_chrome")
    driver.get('https://demoqa.com/dynamic-properties')
    yield driver


@pytest.fixture(scope='function')
def get_elem_id(dynamic_properties):
    driver = dynamic_properties
    element = driver.find_element(By.XPATH,
                                  '//p[text()="This text has random Id"]')
    yield element.get_attribute('id')
