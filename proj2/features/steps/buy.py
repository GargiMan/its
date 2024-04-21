#!/usr/bin/env python3
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils import *
import re

@step(u'I see the featured items')
def step_impl(context):
    assert get_elements_count(context, By.CSS_SELECTOR, "#content .product-thumb") != 0, "No featured items found"


@step(u'I click on {index}. item on page')
def step_impl(context, index):
    get_elements(context, By.CSS_SELECTOR, "#content .product-thumb")[int(index)-1].click()


@step(u'I click on the \'{button}\' button')
def step_impl(context, button):
    if get_elements_count(context, By.XPATH, f"//button[contains(.,'{button}')]") != 0:
        element_click(context, By.XPATH, f"//button[contains(.,'{button}')]")
    else:
        element_click(context, By.XPATH, f"//a[contains(.,'{button}')]")


@step(u'I see the button \'{button}\' is disabled')
def step_impl(context, button):
    assert element_attribute(context, By.XPATH, f"//button[contains(.,'{button}')]", "disabled") is not None, "Button is not disabled"


@step(u'I see the info popup')
def step_impl(context):
    assert get_elements_count(context, By.CSS_SELECTOR, ".alert-success") != 0, "Info popup not displayed"


@step(u'I click on the cart button')
def step_impl(context):
    element_click(context, By.CSS_SELECTOR, "#header-cart button")


@step(u'I see the cart popover without any items')
def step_impl(context):
    assert get_elements_count(context, By.CSS_SELECTOR, "#header-cart") != 0, "Popover is not displayed"
    assert "Your shopping cart is empty!" in element_text(context, By.CSS_SELECTOR, "#header-cart ul"), "Empty cart message not found"
    assert get_elements_count(context, By.CSS_SELECTOR, "#header-cart ul li table") == 0, "Cart is not empty"


@step(u'I see the cart popover with {count} item/s')
def step_impl(context, count):
    assert get_elements_count(context, By.CSS_SELECTOR, "#header-cart") != 0, "Popover is not displayed"
    assert get_elements_count(context, By.XPATH, "//*[@id='header-cart']//li/table//tr") == int(count), "Cart items count mismatch"


@step(u'I see the item in the cart')
def step_impl(context):
    items_count = get_elements_count(context, By.CSS_SELECTOR, "#content table tbody tr")
    assert items_count != 0, "Cart is empty"
    assert items_count == 1, "Multiple items in the cart"
    item_columns = get_elements(context, By.CSS_SELECTOR, "#content table tbody tr td")
    assert item_columns[0].find_element(By.CSS_SELECTOR, "img"), "Item image not found"
    assert item_columns[1].text != "", "Item name not found"
    assert item_columns[2].text != "", "Item model not found"
    assert item_columns[3].find_element(By.CSS_SELECTOR, "input").get_attribute("value") == "1", "Item quantity not found"
    assert re.match(r"^(((\$|£)\d{1,3}(?:[,]\d{3})*(?:[.]\d{2}))|(\d{1,3}(?:[,]\d{3})*(?:[.]\d{2})€))$", item_columns[4].text.strip()) is not None, "Unit price not found"
    assert re.match(r"^(((\$|£)\d{1,3}(?:[,]\d{3})*(?:[.]\d{2}))|(\d{1,3}(?:[,]\d{3})*(?:[.]\d{2})€))$", item_columns[5].text.strip()) is not None, "Total price not found"


@step(u'I continue to view cart with info popup')
def step_impl(context):
    element_click(context, By.CSS_SELECTOR, "#alert a[href*='checkout/cart']")


@step(u'I continue to checkout with the cart popover')
def step_impl(context):
    if get_elements_count(context, By.CSS_SELECTOR, "#header-cart") != 0:
        element_click(context, By.CSS_SELECTOR, "#header-cart button")
    element_click(context, By.CSS_SELECTOR, "#header-cart a[href*='checkout/checkout']")


@step(u'I continue to view cart with the cart popover')
def step_impl(context):
    if get_elements_count(context, By.CSS_SELECTOR, "#header-cart") != 0:
        element_click(context, By.CSS_SELECTOR, "#header-cart button")
    element_click(context, By.CSS_SELECTOR, "#header-cart a[href*='checkout/cart']")


@step(u'I fill out the item required fields')
def step_impl(context):
    selects = get_elements(context, By.CSS_SELECTOR, "#content div[class*=required] select")
    for select in selects:
        if select.is_displayed():
            Select(select).select_by_index(len(Select(select).options)-1)
    
    fields = get_elements(context, By.CSS_SELECTOR, "#content div[class*=required] input[type=text]")
    for field in fields:
        if field.is_displayed():
            element_send_keys(context, field, "test")
    
    checkboxes = get_elements(context, By.CSS_SELECTOR, "#content div[class*=required] input[type=checkbox]")
    for checkbox in checkboxes:
        if checkbox.is_displayed():
            element_click(context, checkbox)
    

@step(u'I see the order form with required fields and default values')
def step_impl(context):
    #required/non-required fields
    assert get_elements_count(context, By.CSS_SELECTOR, "#content div[class*=required]:has(input[type*=radio])") == 1, "Required radio buttons count mismatch"
    assert get_elements_count(context, By.CSS_SELECTOR, "#content div[class*=required]:has(input[type*=text])") == 6, "Required text fields count mismatch"
    assert get_elements_count(context, By.CSS_SELECTOR, "#content div[class*=required]:has(select)") == 2, "Required select fields count mismatch" 
    assert get_elements_count(context, By.CSS_SELECTOR, "#content .input-group") == 2, "Required payment and shipping method fields count mismatch"
    
    assert get_elements_count(context, By.CSS_SELECTOR, "#content #form-register div div:not([class*=required]):has(input[type*=text])") == 2, "Non-required text fields count mismatch"
    
    #default values
    assert element_attribute(context, By.CSS_SELECTOR, "div[class*=required] #input-firstname", "value") == "", "First name default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, "div[class*=required] #input-lastname", "value") == "", "Last name default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, "div[class*=required] #input-email", "value") == "", "Email default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, "#input-shipping-company", "value") == "", "Company default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, "div[class*=required] #input-shipping-address-1", "value") == "", "Address 1 default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, "#input-shipping-address-2", "value") == "", "Address 2 default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, "div[class*=required] #input-shipping-city", "value") == "", "City default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, "div[class*=required] #input-shipping-postcode", "value") == "", "Postcode default value mismatch"
    assert Select(get_element(context, By.CSS_SELECTOR, "div[class*=required] #input-shipping-country")).first_selected_option.text == "United Kingdom", "Country default value mismatch"
    assert Select(get_element(context, By.CSS_SELECTOR, "div[class*=required] #input-shipping-zone")).first_selected_option.text == "--- Please Select ---", "Zone default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, ".input-group #input-payment-method", "value") == "", "Payment method default value mismatch"
    assert element_attribute(context, By.CSS_SELECTOR, ".input-group #input-shipping-method", "value") == "", "Shipping method default value mismatch"


@step(u'I fill out the order details')
def step_impl(context):
    element_click(context, By.CSS_SELECTOR, "#input-guest")
    
    element_send_keys(context, By.CSS_SELECTOR, "#input-firstname", "John")
    element_send_keys(context, By.CSS_SELECTOR, "#input-lastname", "Doe")
    element_send_keys(context, By.CSS_SELECTOR, "#input-email", "john.doe@gmail.com")
    element_send_keys(context, By.CSS_SELECTOR, "#input-shipping-address-1", "123 Main St")
    element_send_keys(context, By.CSS_SELECTOR, "#input-shipping-city", "Anytown")
    element_send_keys(context, By.CSS_SELECTOR, "#input-shipping-postcode", "12345")
    Select(get_element(context, By.CSS_SELECTOR, "#input-shipping-country")).select_by_visible_text("United States")
    Select(get_element(context, By.CSS_SELECTOR, "#input-shipping-zone")).select_by_visible_text("California")
    
    element_click(context, By.CSS_SELECTOR, "#button-register")
    
    element_click(context, By.CSS_SELECTOR, "#button-shipping-methods")
    element_click(context, By.CSS_SELECTOR, "#form-shipping-method input[type=radio]")
    element_click(context, By.CSS_SELECTOR, "#form-shipping-method button[type=submit]")
    
    element_click(context, By.CSS_SELECTOR, "#button-payment-methods")
    element_click(context, By.CSS_SELECTOR, "#form-payment-method input[type=radio]")
    element_click(context, By.CSS_SELECTOR, "#form-payment-method button[type=submit]")


@step(u'I see the order confirmation')
def step_impl(context):
    #assert get_elements_count(context, By.CSS_SELECTOR, ".alert-success") != 0, "Order confirmation not displayed"
    assert "Your order has been placed!" in element_text(context, By.CSS_SELECTOR, "#content"), "Order confirmation message not found"
    assert "Your order has been successfully processed!" in element_text(context, By.CSS_SELECTOR, "#content"), "Order processing message not found"
