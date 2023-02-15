import pytest


@pytest.fixture(scope='class')
def get_checkboxes(request):
    driver = request.getfixturevalue("get_chrome")
    driver.get('https://demoqa.com/checkbox')
    yield driver
