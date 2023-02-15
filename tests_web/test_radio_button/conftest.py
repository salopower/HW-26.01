import pytest


@pytest.fixture(scope='class')
def get_radio_buttons(request):
    driver = request.getfixturevalue("get_chrome")
    driver.get('https://demoqa.com/radio-button')
    yield driver