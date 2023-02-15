from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests_web.test_dynamic_properties.helper import is_element_enabled


class TestDynamicProperties:

    def test_get_id(self, dynamic_properties, get_elem_id):
        random_text_elem = dynamic_properties.find_element(By.ID, get_elem_id)
        assert 'random' in random_text_elem.text

    def test_wait_for_enable_element(self, dynamic_properties):
        locator = (By.CSS_SELECTOR, '#enableAfter')
        WebDriverWait(driver=dynamic_properties, timeout=6).until(EC.element_to_be_clickable(locator))
        enable_button = dynamic_properties.find_element(*locator)
        assert enable_button.is_enabled()

    def test_check_if_element_enabled(self, dynamic_properties):
        locator = (By.CSS_SELECTOR, '#enableAfter')
        assert is_element_enabled(dynamic_properties, locator, 6)

    def test_button_is_present(self, dynamic_properties):
        dynamic_properties.refresh()
        locator = (By.CSS_SELECTOR, "#visibleAfter")
        # wait = WebDriverWait(driver, 10)
        #     wait.until(EC.visibility_of(visible_button))
        #     assert visible_button.is_displayed()
        wait = WebDriverWait(driver=dynamic_properties, timeout=6)
        wait.until(EC.visibility_of_element_located(locator))
        assert dynamic_properties.find_element(*locator).is_displayed()
