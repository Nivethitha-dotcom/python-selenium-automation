from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Locate by XPATH:
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo' and @aria-label='Amazon']")

#Locate by ID:
driver.find_element(By.ID,'ap_email')
driver.find_element(By.ID,'continue')

# Locate by parent -> child:
driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-top-medium a-size-small']//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-top-medium a-size-small']//a[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//a[@class='a-expander-header a-declarative a-expander-inline-header a-link-expander']//span[@class='a-expander-prompt']")


driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom' and @class='a-link-normal']")
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link' and @class='a-link-normal']")

driver.find_element(By.ID, 'createAccountSubmit')