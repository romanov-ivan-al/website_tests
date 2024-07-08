from baseapp import BasePage
from sbispage import SbisPage, SbisLocators
from selenium import webdriver
import time


def test_click_button(browser):
    sbis_page = SbisPage(browser)
    sbis_page.go_to_page()
    sbis_page.click_button_contacts()
    time.sleep(5)
    sbis_page.click_tenzor_banner()
    time.sleep(5)
    sbis_page.go_to_new_page()
    time.sleep(5)
    text = sbis_page.find_sila_v_ludiah()
    assert text == 'Сила в людях'
    sbis_page.click_tenzor_about()
    time.sleep(5)
    
    


    
