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
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dap_frn_logo%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(5)

#Locate by CSS_SELECTOR by using tag and class:
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")
#Locate by CSS_SELECTOR by using tag and class:
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
#Locate by CSS_SELECTOR by using tag and id:
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
#Locate by CSS_SELECTOR by using tag and id:
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
#Locate by CSS_SELECTOR by using id and attribute:
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check[name='passwordCheck']")
#Locate by CSS_SELECTOR by using id and class:
driver.find_element(By.CSS_SELECTOR, "input#continue.a-button-input")
#Locate by CSS_SELECTOR by using tag and place holder with partial match:
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_condition_of_use']")
#Locate by CSS_SELECTOR by using Parent => child and place holder with partial match:
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='ap_register_notification_privacy_notice']")
#Locate by CSS_SELECTOR by using tag with class and place holder with partial match:
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin']")