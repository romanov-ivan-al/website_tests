from baseapp import BasePage
from sbispage import SbisPage, SbisLocators
from selenium import webdriver


def test_click_button(browser):
    sbis_page = SbisPage(browser)
    sbis_page.go_to_page()

    sbis_page.click_button_contacts()


    
