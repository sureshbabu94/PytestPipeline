import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def test_chrome():
    ser=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=ser)
    driver.get('https://www.fedex.com')
    driver.maximize_window()
    time.sleep(5)
    driver.save_screenshot('Chrome_home.png')
    driver.close()

def test_firefox():
    ser=Service(GeckoDriverManager().install())
    driver=webdriver.Firefox(service=ser)
    driver.get('https://www.fedex.com')
    time.sleep(5)
    driver.maximize_window()
    driver.save_screenshot('Firefox_home.png')
    driver.close()
