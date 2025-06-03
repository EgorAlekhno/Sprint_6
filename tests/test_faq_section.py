import time

import allure
import pytest

from data import FAQ_ANSWERS
from pages.main_page import MainPage


class TestFaqSection:
    @pytest.mark.parametrize("index, expected_text", list(enumerate(FAQ_ANSWERS)))
    @allure.title("Проверка текста ответа на вопрос в FAQ под индексом: {index}")
    def test_check_question_answer_by_index(self, driver, index, expected_text):
        page = MainPage(driver)
        page.accept_cookies()
        page.click_question_by_index(index)
        actual_text = page.get_answer_text_by_index(index)
        assert actual_text == expected_text
