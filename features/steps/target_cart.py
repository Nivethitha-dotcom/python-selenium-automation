from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()
    sleep(5)


@then('Verify your cart is empty message is shown')
def verify_cart_is_empty(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_result = 'Your cart is empty'
    assert actual_result == expected_result, f'Expected {expected_result}, got actual {actual_result}'
    print('Test case passed')
