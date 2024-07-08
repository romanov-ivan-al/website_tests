from baseapp import BasePage
from sbispage import SbisPage, SbisLocators
from selenium import webdriver
import time
from loguru import logger

logger.add("file.log", rotation="500 MB") 

def test_scenario_number_one(browser):
    logger.info("Тест сценария No1")
    sbis_page = SbisPage(browser)
    sbis_page.go_to_page()
    sbis_page.click_button_contacts()
    sbis_page.click_tenzor_banner()
    sbis_page.go_to_new_page()
    text = sbis_page.find_sila_v_ludiah()
    assert text == 'Сила в людях'
    sbis_page.click_tenzor_about()
    assert "https://tensor.ru/about" in sbis_page.driver.current_url
    element = sbis_page.find_working_block()
    text = element.text
    assert text == 'Работаем'
    assert sbis_page.check_img() == True


def test_scenario_number_two(browser):
    logger.info("Тест сценария No2")

    


    
    
    
