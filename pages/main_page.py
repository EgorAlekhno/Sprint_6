import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Подтверждение куки')
    def accept_cookies(self):
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Клик по кнопке "Заказать" в хедере')
    def click_top_order_button(self):
        self.find_element_with_wait(MainPageLocators.TOP_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Клик по кнопке "Заказать" внизу')
    def scroll_to_how_it_works_and_click_order(self):
        self.scroll_to_element(MainPageLocators.HOW_IT_WORKS_SECTION)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_IN_HOW_IT_WORKS_SECTION)

    @allure.step('Скролл до блока FAQ и клик на вопрос {index}')
    def click_question_by_index(self, index):
        question_formatted_locator = self.format_locators(MainPageLocators.QUESTION, index)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION)
        self.click_to_element(question_formatted_locator)

    @allure.step('Получение текста ответа на вопрос {index}')
    def get_answer_text_by_index(self, index):
        answer_formatted_locator = self.format_locators(MainPageLocators.ANSWER, index)
        return self.get_text_from_element(answer_formatted_locator)

    @allure.step('Клик по лого "Самоката"')
    def click_scooter_logo(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Клик по лого "Яндекс"')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Клик по лого "Яндекс"')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO)
