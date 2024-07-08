from baseapp import BasePage
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisLocators:
    LOCATOR_BUTTON_CONTACTS = (By.CSS_SELECTOR, "a[href='/contacts']")


class SbisPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url="https://sbis.ru")

    def click_button_contacts(self):
        # element = self.driver.find_element(*SbisLocators.LOCATOR_BUTTON_CONTACTS)
        # element.click()
        # ActionChains(self.driver).move_to_element(element).click()
        # self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.element_to_be_clickable(SbisLocators.LOCATOR_BUTTON_CONTACTS ))
        elem.click()
        

        


    

       



    