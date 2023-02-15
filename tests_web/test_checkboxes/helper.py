from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def set_checkbox_state(driver: WebDriver, fold_name: str, is_enabled: bool = True) -> None:
    folder = driver.find_element(
        By.XPATH,
        f'//span[@class="rct-title"][.="{fold_name}"]'
        f'//ancestor::span[@class="rct-text"]')
    _ = folder.location_once_scrolled_into_view
    fold_input = folder.find_element(By.CSS_SELECTOR, 'input[id]')
    fold_checkbox = folder.find_element(By.CSS_SELECTOR, 'label[for]')
    if is_enabled:
        if not fold_input.is_selected():
            fold_checkbox.click()
    else:
        if fold_input.is_selected():
            fold_checkbox.click()


def select_fold(driver: WebDriver, fold_name: str, enabled=True):
    set_checkbox_state(driver, fold_name, is_enabled=enabled)


def select_folders(driver: WebDriver = None, folders: list = None):
    if folders:
        for folder in folders:
            select_fold(driver, folder, enabled=True)


def expand_all_folders(driver: WebDriver):
    expand_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Expand all"]')
    expand_button.click()


def optimize_test_data(data: list):
    return {'tree': [d.capitalize() for d in data],
            'results': [r.lower() for r in data]}


def expand_fold(driver: WebDriver, folder_name: str):
    expand_button = driver.find_element(By.XPATH, f'//span[@class="rct-text"][.="{folder_name}"]'
                                                  f'/button[@aria-label="Toggle"]')
    _ = expand_button.location_once_scrolled_into_view
    expand_button.click()


def expand_folders(driver: WebDriver, folders: list):
    for folder in folders:
        expand_fold(driver, folder)

