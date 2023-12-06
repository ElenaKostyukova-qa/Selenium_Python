import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://testqastudio.me/"

def test_smoke(browser):
    """
    Test case WERT-1. Smoke test
    """
    browser.get(url=URL)

    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
    element.click()
    sku = browser.find_element(by=By.CLASS_NAME, value="sku")

    assert sku.text == 'C0MSSDSUM7',  "Unexpected sku"

    

