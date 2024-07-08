from baseapp import BasePage
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisLocators:
    LOCATOR_BUTTON_CONTACTS = (By.CSS_SELECTOR, "a[href='/contacts']")
    TENZOR_BANNER = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
    SILA_V_LUDIAH = (By.XPATH, "//p[contains(@class, 'tensor_ru-Index__card-title') and contains(@class, 'tensor_ru-pb-16') and contains(text(), 'Сила в людях')]")


class SbisPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url="https://sbis.ru")

    def click_button_contacts(self):
        return self.find_element(SbisLocators.LOCATOR_BUTTON_CONTACTS).click()
    
    def click_tenzor_banner(self):
        return self.find_element(SbisLocators.TENZOR_BANNER).click()
    
    def go_to_new_page(self):
        new = self.driver.window_handles
        print(new, "ALL HANDLES")
        self.driver.switch_to.window(new[-1])




        

        


    

       



    