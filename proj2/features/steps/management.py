#!/usr/bin/env python3
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils import *

@step(u'I open the catalog of \'{category}\'')
def step_impl(context, category):
    element_click(context, By.XPATH, f"//nav//li[@id='menu-catalog']")
    element_click(context, By.XPATH, f"//nav//li[@id='menu-catalog']//li//a[contains(.,'{category}')]")
    wait_until_on_page(context.drv, "http://opencart:8080/administration/index.php?route=catalog")

    
@step(u'I see product list with columns')
def step_impl(context):
    # 6 + 1 for checkboxes
    assert get_elements_count(context, By.CSS_SELECTOR, "#content table thead td") == 7, "Columns count mismatch"
    columns = get_elements(context, By.CSS_SELECTOR, "#content table thead td")
    columns_text = [column.text.strip() for column in columns][1:]
    for row in context.table:
        assert row[0] in columns_text, f"Column {row[0]} not found in {columns_text}"
    
    
@step(u'I see filter section with fields')
def step_impl(context):
    assert get_elements_count(context, By.CSS_SELECTOR, "#content #filter-product") == 1, "Filter section not found"
    fields = get_elements(context, By.CSS_SELECTOR, "#content #filter-product label")
    fields_text = [field.text.strip() for field in fields]
    for row in context.table:
        assert row[0] in fields_text, f"Filter field {row[0]} not found in {fields_text}"
        
    
@step(u'I see buttons for product list management')
def step_impl(context):
    assert get_elements_count(context, By.CSS_SELECTOR, "#content .page-header .float-end > *") != 3, "Buttons count mismatch"
    buttons = get_elements(context, By.CSS_SELECTOR, "#content .page-header .float-end > *")[1:]
    buttons_text = [button.get_attribute("title").strip() for button in buttons]
    for row in context.table:
        assert row[0] in buttons_text, f"Button {row[0]} not found in {buttons_text}"
      
      
@step(u'I click on edit button for {index}. product')
def step_impl(context, index):
    get_elements(context, By.CSS_SELECTOR, f"table tbody tr a[title*=Edit]")[int(index)-1].click()
    

@step(u'I go to \'{tab}\' tab')
def step_impl(context, tab):
    element_click(context, By.XPATH, f"//form//ul//a[contains(.,'{tab}')]") 
        
        
@step(u'I see stock section with fields')
def step_impl(context):
    section_names = [section.text.strip() for section in get_elements(context, By.CSS_SELECTOR, "#tab-data fieldset legend")]
    assert section_names.index('Stock') == 2, "Stock section not found"
    section_fields = [section.text.strip() for section in get_elements(context, By.CSS_SELECTOR, f"#tab-data fieldset:nth-of-type({section_names.index('Stock')+1}) label")]
    for row in context.table:
        assert row[0] in section_fields, f"Field {row[0]} not found in {section_fields}"
    
    
@step(u'I set \'{value}\' value to \'{field}\' field')
def step_impl(context, value, field):
    element_send_keys(context, By.XPATH, f"//label[contains(.,'{field}')]/..//input", value)
    
    
@step(u'I save the product changes')
def step_impl(context):
    element_click(context, By.CSS_SELECTOR, "button[title=Save]")
    
    
@step(u'I see success saving message')
def step_impl(context):
    assert get_elements_count(context, By.CSS_SELECTOR, ".alert-success") != 0, "Success message not found"
    
    
@step(u'I see \'{value}\' value in \'{field}\' field')
def step_impl(context, value, field):
    assert element_attribute(context, By.XPATH, f"//label[contains(.,'{field}')]/..//input", "value") == value, "Value mismatch"
    
    
@step(u'I go back to the product list')
def step_impl(context):
    element_click(context, By.CSS_SELECTOR, "a[title=Back]")
    
    
@step(u'I see {index}. product with \'{value}\' value in \'{column}\' column')
def step_impl(context, index, value, column):
    column_index = [column.text.strip() for column in get_elements(context, By.CSS_SELECTOR, "#content table thead td")].index(column) + 1
    assert element_text(context, By.XPATH, f"//table//tr[{int(index)}]/td[{column_index}]//span") == value, "Value mismatch"
    
    
@step(u'I select \'{option}\' in \'{field}\' dropdown')
def step_impl(context, option, field):
    element_click(context, By.XPATH, f"//label[contains(.,'{field}')]/..//select/option[contains(.,'{option}')]")
    

@step(u'I see option \'{option}\' selected in \'{field}\' dropdown')
def step_impl(context, option, field):
    assert option in Select(get_element(context, By.XPATH, f"//label[contains(.,'{field}')]/..//select")).first_selected_option.text, "Option not selected"
    
    
@step(u'I toggle \'{toggle}\' option')
def step_impl(context, toggle):
    context.prev_toggle = get_elements(context, By.XPATH, f"//label[contains(.,'{toggle}')]/..//input")[1].get_attribute("checked")
    element_click(context, By.XPATH, f"//label[contains(.,'{toggle}')]/..//input/..")
    
    
@step(u'I see saved \'{toggle}\' option')
def step_impl(context, toggle):
    assert get_elements(context, By.XPATH, f"//label[contains(.,'{toggle}')]/..//input")[1].get_attribute("checked") is not context.prev_toggle, "Option not saved"

