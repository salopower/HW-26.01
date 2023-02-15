from selenium.webdriver.common.by import By

from tests_web.test_checkboxes.helper import set_checkbox_state, select_fold, select_folders, expand_all_folders, \
    optimize_test_data, expand_fold, expand_folders


class TestCheckBoxes:

    def test_checkboxes(self, get_checkboxes):
        driver = get_checkboxes
        folders = ['Commands', 'General', 'Private']
        expand_all_folders(driver)
        select_folders(driver, optimize_test_data(folders).get('tree'))
        result = driver.find_element(By.CSS_SELECTOR, 'div#result').text.split(':')[1].split()
        assert sorted(result) == sorted(optimize_test_data(folders).get('results'))

    def test_checkboxes_bonus(self, get_checkboxes):
        driver = get_checkboxes
        folders = ['Home', 'Documents', 'Office']
        target_folder = 'General'
        expand_folders(driver, folders)
        select_fold(driver, target_folder)
        result = driver.find_element(
            By.CSS_SELECTOR, 'div#result').text.split(':')[1].split()
        assert all([len(result) == 1, target_folder.lower() == result[0]])