import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
