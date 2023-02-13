import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

driver = Chrome(executable_path='C:\DRIVERS\chromedriver_win32\chromedriver.exe')


@pytest.fixture
def radio_button():
    driver.get('https://demoqa.com/radio-button')


def test_active_yes_radio(radio_button):
    input_yes = driver.find_element(By.CSS_SELECTOR, '#yesRadio')
    label_yes = driver.find_element(By.CSS_SELECTOR, '[for="yesRadio"')
    label_yes.click()
    is_input_selected = input_yes.is_selected()
    result_text = driver.find_element(By.CSS_SELECTOR, 'span.text-success').text
    assert is_input_selected and result_text == 'Yes'


def test_get_radio_buttons_info(radio_button):
    radio_buttons = driver.find_elements(By.CSS_SELECTOR, '[type="radio"]')
    radio_buttons_data = {}
    for button in radio_buttons:
        button_name = button.get_attribute('id')
        button_enabled = button.is_enabled()
        button_selected = button.is_selected()
        radio_buttons_data[button_name] = {"Enabled": button_enabled, "Selected": button_selected}
    print(f'\n{radio_buttons_data}')


def test_activate_disabled_radio_button(radio_button):
    no_radio_button = driver.find_element(By.CSS_SELECTOR, '[for="noRadio"]')
    input_no_radio_button = driver.find_element(By.CSS_SELECTOR,'[id="noRadio"]')
    driver.execute_script("arguments[0].removeAttribute('disabled','disabled')", input_no_radio_button)
    no_radio_button.click()
    is_no_radio_button_selected = input_no_radio_button.is_selected()
    assert is_no_radio_button_selected

