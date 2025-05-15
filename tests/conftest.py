
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1440, 1000)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
