#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

def get_driver():
    '''Get Chrome/Firefox driver from Selenium Hub'''
    try:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(15)

    # Web stranku ziskate nasledujicim:
    # (jedno nebo druhe, zalezi na nastaveni prostedi)
    # driver.get("http://opencart:8080/")
    # driver.get("http://localhost:8080/")

    return driver

    # Nezapomente vzdy po ukonceni testovani zavrit driver:
    # driver.close() nebo .quit()
