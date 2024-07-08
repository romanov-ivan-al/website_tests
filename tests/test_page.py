from baseapp import BasePage
from sbispage import SbisPage, SbisLocators
from selenium import webdriver
import time
from loguru import logger


def test_scenario_number_one(browser):
    logger.add("scenario_one.log", rotation="500 MB") 
    sbis_page = SbisPage(browser)
    sbis_page.go_to_page()
    sbis_page.click_button_contacts()
    #time.sleep(5)
    sbis_page.click_tenzor_banner()
    #time.sleep(5)
    sbis_page.go_to_new_page()
    #time.sleep(5)
    text = sbis_page.find_sila_v_ludiah()
    assert text == 'Сила в людях'
    sbis_page.click_tenzor_about()
    #time.sleep(5)
    assert "https://tensor.ru/about" in sbis_page.driver.current_url
    #time.sleep(5)
    element = sbis_page.find_working_block()
    text = element.text
    assert text == 'Работаем'
    assert sbis_page.check_img() == True


    
    
    
