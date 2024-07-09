from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go_to_page(self):
        return self.driver.get(self.url)

    def find_element(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        return wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        return wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
