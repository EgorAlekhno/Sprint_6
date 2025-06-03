
import pytest
from selenium import webdriver

from data import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1440, 1000)
    driver.get(Urls.BASE)
    yield driver
    driver.quit()
