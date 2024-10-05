from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Click sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(5)


@when('Click sign in from the right side navigation menu')
def click_sign_in_right_side_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()
    sleep(10)



@then('Verify sign in form opened')
def verify_sign_in_form_opened(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected_result = 'Sign into your Target account'
    assert actual_result == expected_result, f'Expected {expected_result}, got actual {actual_result}'
    print('Test case passed')
