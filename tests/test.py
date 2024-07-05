from BaseApp import Browser
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)

browser = Browser(driver, "https://www.google.com/")
page = browser.go_to_page()

browser.quit()