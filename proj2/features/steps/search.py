#!/usr/bin/env python3
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils import *

@step(u'I see the search page')
def step_impl(context):
    assert "http://opencart:8080/index.php?route=product/search" in context.drv.current_url, "Not on search page"


@step(u'I click on the search button')
def step_impl(context):
    element_click(context, By.CSS_SELECTOR, "#search button")


@step(u'I search for \'{item}\' in search bar')
def step_impl(context, item):
    element_send_keys(context, By.CSS_SELECTOR, "#search input", item)
    element_click(context, By.CSS_SELECTOR, "#search button")


@step(u'I search for \'{item}\'')
def step_impl(context, item):
    element_send_keys(context, By.CSS_SELECTOR, "#content #input-search", item)
    element_click(context, By.CSS_SELECTOR, "#content #button-search")


@step(u'I select \'{category}\' in category dropdown')
def step_impl(context, category):
    #Select(get_element(context, By.CSS_SELECTOR, "#content #input-category")).select_by_visible_text(category)
    element_click(context, By.XPATH, f"//*[@id='content']//select[@id='input-category']/option[contains(.,'{category}')]")


@step(u'I see selected value \'{category}\' in category dropdown')
def step_impl(context, category):
    assert category in Select(get_element(context, By.CSS_SELECTOR, "#content #input-category")).first_selected_option.text, "Category not selected"


@step(u'I see the search categories')
def step_impl(context):
    options = Select(get_element(context, By.CSS_SELECTOR, "#content #input-category")).options
    options_text = [option.text.strip() for option in options]
    for row in context.table:
        assert row[0] in options_text, f"Category {row[0]} not found in {options_text}"


@step(u'I see no search results')
def step_impl(context):
    assert get_elements_count(context, By.XPATH, "//p[contains(.,'There is no product that matches the search criteria.')]") != 0, "Search results displayed"
    assert get_elements_count(context, By.CSS_SELECTOR, "#product-list") == 0


@step(u'I see some search results')
def step_impl(context):
    assert get_elements_count(context, By.CSS_SELECTOR, "#product-list") != 0, "Search results not displayed"


@step(u'I check checkbox \'{checkbox}\'')
def step_impl(context, checkbox):
    element_click(context, By.XPATH, f"//label[contains(.,'{checkbox}')]/../input")


@step(u'I see the checkbox \'{checkbox}\' is disabled')
def step_impl(context, checkbox):
    assert get_element(context, By.XPATH, f"//label[contains(.,'{checkbox}')]/../input").get_attribute("disabled") is not None, "Checkbox is not disabled"
