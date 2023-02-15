import time
from selenium.common import WebDriverException, InvalidElementStateException


def is_element_enabled(driver, locator, timeout):
    is_enabled = False
    end_time = time.monotonic() + timeout
    is_element_in_dom(driver, locator)
    while time.monotonic() <= end_time:
        if driver.find_element(*locator).is_enabled():
            is_enabled = True
            break
        else:
            continue
    if is_enabled:
        return True
    else:
        raise InvalidElementStateException(
            f'element is present in DOM,'
            f' but not enabled after {timeout + 1} sec.')



def is_element_in_dom(driver, locator):
    try:
        _ = driver.find_element(*locator)
        return True
    except WebDriverException:
        raise
