import time

import allure

from data import DATE
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнение поля "Имя"')
    def fill_name_field(self, name):
        self.add_text_to_element(OrderPageLocators.FIRST_NAME_FIELD, name)
        return self

    @allure.step('Заполнение поля "Фамилия"')
    def fill_lastname_field(self, last_name):
        self.add_text_to_element(OrderPageLocators.LAST_NAME_FIELD, last_name)
        return self

    @allure.step('Заполнение поля "Адрес"')
    def fill_address_name_field(self, address):
        self.add_text_to_element(OrderPageLocators.ADDRESS_NAME_FIELD, address)
        return self

    @allure.step('Выбор станции "Метро"')
    def choose_station(self, station):
        self.click_to_element(OrderPageLocators.METRO_STATION_FIELD)
        self.add_text_to_element(OrderPageLocators.METRO_STATION_FIELD, station)
        self.click_to_element(OrderPageLocators.SELECTED_STATION)
        return self

    @allure.step('Заполнение поля "Телефон"')
    def fill_phone_field(self, number):
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, number)
        return self

    @allure.step('Клик по кнопке "Далее"')
    def click_on_next_button(self):
        self.click_to_element(OrderPageLocators.CONTINUE_BUTTON)

    @allure.step('Проверка отображения заголовка второй формы')
    def check_the_title_of_second_form_displaying(self):
        self.is_element_visible(OrderPageLocators.TITLE_ABOUT_RENT_FORM)

    @allure.step("Подождать появления поля даты привоза самоката")
    def wait_visibility_of_date_input(self):
        self.find_element_with_wait(OrderPageLocators.DATE_INPUT)

    @allure.step("Заполнить поле даты привоза самоката")
    def fill_current_date(self, date):
        self.fill_date(OrderPageLocators.DATE_INPUT, date)

    @allure.step('Заполнить поле "Срок аренды"')
    def set_rental_duration(self):
        self.click_to_element(OrderPageLocators.RENTAL_DURATION_FIELD)
        self.find_element_with_wait(OrderPageLocators.RENTAL_DURATION_LIST)
        self.click_to_element(OrderPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD)

    @allure.step('Выбор цвета самоката с помощью чекбокса')
    def set_color_field(self):
        self.click_to_element(OrderPageLocators.CHECKBOX_BLACK)
        return self

    @allure.step('Добавление комментария для курьера')
    def set_comment_field(self, comment):
        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, comment)
        return self

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.find_element_with_wait(OrderPageLocators.POP_UP_CONFIRM_ORDER)

    @allure.step('Проверка отображения окна подтверждения после нажатия кнопки Заказать')
    def check_displaying_of_confirm_window(self):
        self.is_element_visible(OrderPageLocators.POP_UP_CONFIRM_ORDER)

    @allure.step("Проверка отображения попапа успешного оформления заказа")
    def is_order_success_popup_displayed(self):
        return self.find_element_with_wait(OrderPageLocators.COMPLETE_ORDER_POP_UP).is_displayed()

    @allure.step('Нажать кнопку "Да" в окне подтверждения заказа')
    def click_yes_button_confirmation_pop_up(self):
        self.click_to_element(OrderPageLocators.YES_POP_BUTTON)
        self.find_element_with_wait(OrderPageLocators.COMPLETE_ORDER_POP_UP)
        return self

    @allure.step('Заполнение первой формы')
    def personal_information_input(self, name, last_name, address, station, number):
        self.fill_name_field(name)
        self.fill_lastname_field(last_name)
        self.fill_address_name_field(address)
        self.choose_station(station)
        self.fill_phone_field(number)
        self.click_on_next_button()
        self.check_the_title_of_second_form_displaying()

    #
    @allure.step('Заполнение второй части формы и окно подтверждения')
    def rental_information_input(self, comment):
        self.wait_visibility_of_date_input()
        self.fill_current_date(DATE)
        self.set_rental_duration()
        self.set_color_field()
        self.set_comment_field(comment)
        self.click_order_button()
        self.check_displaying_of_confirm_window()
