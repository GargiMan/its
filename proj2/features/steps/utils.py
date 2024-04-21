#!/usr/bin/env python3
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support.expected_conditions import *
import time

WAIT_TIMEOUT=10
PAGE_LOAD_TIMEOUT=20

ADMID_USERNAME="user"
ADMID_PASSWORD="bitnami"

def wait_until_page_loaded(drv):
    try:
        WebDriverWait(drv, PAGE_LOAD_TIMEOUT).until(lambda drv: drv.execute_script('return document.readyState') == 'complete')
    except TimeoutException:
        print("Loading page took too much time!")


def wait_until_on_page(drv, url):
    try:
        WebDriverWait(drv, WAIT_TIMEOUT).until(lambda drv: url in drv.current_url)
    except TimeoutException:
        print(f"Not on page {url}")


def get_element(context, by, value):
    try:
        WebDriverWait(context.drv, WAIT_TIMEOUT).until(visibility_of_element_located((by, value)))
    except TimeoutException:
        print(f"Element {value} not found")
        return None
    element = context.drv.find_element(by, value)
    try:
        element.is_displayed()
        context.drv.execute_script("arguments[0].scrollIntoView();", element)
    except StaleElementReferenceException:
        return get_element(context, by, value)
    return element


def get_element_present(context, by, value):
    try:
        WebDriverWait(context.drv, WAIT_TIMEOUT).until(presence_of_element_located((by, value)))
    except TimeoutException:
        print(f"Element {value} not found")
        return None
    element = context.drv.find_element(by, value)
    try:
        context.drv.execute_script("arguments[0].scrollIntoView();", element)
    except StaleElementReferenceException:
        return get_element_present(context, by, value)
    return element


def get_elements(context, by, value):
    return context.drv.find_elements(by, value)


def get_elements_count(context, by, value):
    return len(get_elements(context, by, value))


def element_click(context, by, value):
    try:
        get_element(context, by, value).click()
    except ElementClickInterceptedException:
        close_popups(context)
        get_element(context, by, value).click()


def element_send_keys(context, by, value, keys):
    element = get_element(context, by, value)
    element.clear()
    element.send_keys(keys)


def element_text(context, by, value):
    return get_element(context, by, value).text


def element_attribute(context, by, value, attribute):
    return get_element_present(context, by, value).get_attribute(attribute)


def scroll_to_bottom(context):
    context.drv.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def close_popups(context):
    for close in get_elements(context, By.CSS_SELECTOR, ".btn-close"):
        close.click()


@step(u'I am on the homepage')
def step_impl(context):
    context.drv.get("http://opencart:8080/")

    wait_until_page_loaded(context.drv)


@step(u'I am on the administration page and logged in')
def step_impl(context):
    context.drv.get("http://opencart:8080/administration")

    element_send_keys(context, By.CSS_SELECTOR, "#input-username", ADMID_USERNAME)
    element_send_keys(context, By.CSS_SELECTOR, "#input-password", ADMID_PASSWORD)
    element_click(context, By.CSS_SELECTOR, "button[type='submit']")
    
    wait_until_page_loaded(context.drv)


@step(u'I refresh the page')
def step_impl(context):
    context.drv.refresh()
    
    wait_until_page_loaded(context.drv)