import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с использованием явного ожидания')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание URL страницы')
    def wait_for_url_to_be(self, expected_url):
        return WebDriverWait(self.driver, 6).until(EC.url_to_be(expected_url))

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 6).until(lambda d: len(d.window_handles) > 1)
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)

    def wait_for_title_contains(self, text):
        return WebDriverWait(self.driver, 6).until(EC.title_contains(text))

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Кликнуть по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    @allure.step('Добавление текста элементу')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Заполнение поля ')
    def fill_date(self, locator, date):
        self.driver.find_element(*locator).send_keys(date)
        self.driver.find_element(*locator).send_keys(Keys.RETURN)

    @allure.step('Проверить отображение элемента')
    def is_element_visible(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

    @staticmethod
    def format_locators(locator_1, index):
        method, locator = locator_1
        locator = locator.format(index)
        return method, locator
