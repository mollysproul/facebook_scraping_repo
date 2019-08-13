from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

FB_LOGIN_EMAIL = "your-email@gmail.com"
FB_LOGIN_PASSWORD = "your-password123"


def main():
    login_to_facebook()


# Requires: chromedriver is in the same directory that this .py file is in (otherwise, change executable path below)
# Modifies: none
# Effects: Returns a "driver" that is logged into facebook via the email & password at top of this .py file
def login_to_facebook():
    print("Running login_to_facebook()")

    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_argument(" — incognito")
    # chromeOptions.add_argument('headless')

    driver = webdriver.Chrome(executable_path='chromedriver', options=chromeOptions)

    driver.get('https://www.facebook.com/')
    username_box = driver.find_element_by_id('email')
    username_box.send_keys(FB_LOGIN_EMAIL)
    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(FB_LOGIN_PASSWORD)
    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()

    print("inside facebook")
    return driver


if __name__ == "__main__":
    main()
