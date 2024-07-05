from selenium import webdriver



class Browser:
    "Класс для работы с веб сайтами"
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go_to_page(self):
        return self.driver.get(self.url)


    def quit(self):
        self.driver.quit()


