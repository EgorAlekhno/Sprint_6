import allure
import pytest
from data import user_1, user_2

from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestOrderForm:

    @allure.title('Проверка заказа самоката через верхнюю кнопку "Заказать')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [user_1])
    def test_complete_order_form_order_button_header(self, driver, name, last_name, address, station, number, comment):
        main_page = MainPage(driver)
        main_page.click_top_order_button()

        order_page = OrderPage(driver)
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()

        assert order_page.is_order_success_popup_displayed(), \
            "Попап об успешном заказе не отобразился"

    @allure.title('Проверка заказа самоката через нижнюю кнопку "Заказать')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [user_2])
    def test_complete_order_form_order_button_body(self, driver, name, last_name, address, station, number, comment):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.scroll_to_how_it_works_and_click_order()

        order_page = OrderPage(driver)
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()

        assert order_page.is_order_success_popup_displayed(), \
            "Попап об успешном заказе не отобразился"
