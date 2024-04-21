#!/usr/bin/env python3
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def get_driver():
    """Get Chrome/Firefox driver from Selenium Hub"""
    try:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.ChromeOptions())
    except WebDriverException:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.FirefoxOptions())
    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver


def before_all(context):
    context.drv = get_driver()


def after_all(context):
    if hasattr(context, 'drv'):
        context.drv.quit()


def before_scenario(context, scenario):
    if not hasattr(context, 'drv'):
        context.drv = get_driver()
    context.drv.delete_all_cookies()
