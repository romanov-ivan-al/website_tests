from sbispage import SbisPage
import time
from loguru import logger

logger.add("file.log", rotation="500 MB")


def test_scenario_number_one(browser):
    logger.info("ЗАПУСК СЦЕНАРИЯ N1")
    sbis_page = SbisPage(browser)
    sbis_page.go_to_page()
    sbis_page.click_button_contacts()
    sbis_page.click_tenzor_banner()
    sbis_page.go_to_new_page()
    text = sbis_page.find_sila_v_ludiah()
    assert text == "Сила в людях"
    sbis_page.click_tenzor_about()
    assert "https://tensor.ru/about" in sbis_page.driver.current_url
    element = sbis_page.find_working_block()
    text = element.text
    assert text == "Работаем"
    assert sbis_page.check_img() is True


def test_scenario_number_two(browser):
    logger.info("ЗАПУСК СЦЕНАРИЯ N2")
    sbis_page = SbisPage(browser)
    sbis_page.go_to_page()
    sbis_page.click_button_contacts()
    assert "Новосибирск" == sbis_page.find_location().text
    pattern_contacts_nsk = [
        "СБИС - Новосибирск",
        "ЦентрИнформ",
        "Центр информационной безопасности",
    ]
    contacts = sbis_page.find_contacts()
    assert (
        contacts[0] == pattern_contacts_nsk[0]
        and contacts[1] == pattern_contacts_nsk[1]
        and contacts[2] == pattern_contacts_nsk[2]
    )
    sbis_page.click_region()
    sbis_page.click_kamchtka_region()
    time.sleep(10)  # это не очень хорошая практика, но пока так
    assert "Петропавловск-Камчатский" == sbis_page.find_location().text
