from baseapp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SbisLocators:
    LOCATOR_BUTTON_CONTACTS = (By.CSS_SELECTOR, "a[href='/contacts']")


class SbisPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url="https://sbis.ru/contacts")

    def click_button_contacts(self):
        element = self.driver.find_element(*SbisLocators.LOCATOR_BUTTON_CONTACTS)
        return ActionChains(self.driver).move_to_element(element).click().perform()

        


    

       



    