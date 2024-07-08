from baseapp import BasePage
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

class SbisLocators:
    LOCATOR_BUTTON_CONTACTS = (By.CSS_SELECTOR, "a[href='/contacts']")
    TENZOR_BANNER = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
    SILA_V_LUDIAH = (By.XPATH, "//p[contains(@class, 'tensor_ru-Index__card-title') and contains(@class, 'tensor_ru-pb-16') and contains(text(), 'Сила в людях')]")
    TENZOR_ABOUT = (By.CSS_SELECTOR, "a[href='/about'].tensor_ru-link.tensor_ru-Index__link")
    WORKING_BLOCK = (By.XPATH, "//h2[contains(@class, 'tensor_ru-header-h2') and contains(@class, 'tensor_ru-About__block-title') and text()='Работаем']")
    IMG = (By.XPATH, "//img[contains(@class, 'tensor_ru-About__block3-image') and contains(@class, 'new_lazy') and contains(@class, 'loaded')]")



class SbisPage(BasePage):

    def __init__(self, driver):
        logger.info("SbisPage инициализирован.")
        super().__init__(driver, url="https://sbis.ru")
        

    def click_button_contacts(self):
        logger.info("Нажатие на кнопку 'Контакты'")
        return self.find_element(SbisLocators.LOCATOR_BUTTON_CONTACTS).click()
    
    def click_tenzor_banner(self):
        logger.info("Нажатие на баннер 'Тензор'")
        return self.find_element(SbisLocators.TENZOR_BANNER).click()
    
    def go_to_new_page(self):
        new = self.driver.window_handles
        self.driver.switch_to.window(new[-1])
        logger.info("Переход на новую вкладку")

    def find_sila_v_ludiah(self):
        logger.info("Нахождение элемента 'Сила в людях'")
        return self.find_element(SbisLocators.SILA_V_LUDIAH).text
    
    def click_tenzor_about(self):
        element = self.find_element(SbisLocators.TENZOR_ABOUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        logger.info("Нажатие на элемент 'Подробнее'")
        return element.click()
    
    def find_working_block(self):
        logger.info("Нахождение элемента 'Работаем'")
        return self.find_element(SbisLocators.WORKING_BLOCK)

    
    def check_img(self):
        working_block = self.find_element(SbisLocators.WORKING_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView();", working_block)
        imgs = self.find_elements(SbisLocators.IMG, time=200)
        width = []
        hight = []
        for img in imgs:
            width.append(img.size['width'])
            hight.append(img.size['height'])
            logger.info(f"Проверка размеров изображения: {img.size['width']}, {img.size['height']}")
        return all(i == width[0] for i in width) and all(i == hight[0] for i in hight)
        

    




        

        


    

       



    