from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    SELECTED_STATION = (By.XPATH, ".//li[@class='select-search__row']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    TITLE_ABOUT_RENT_FORM = (By.CLASS_NAME, 'Order_Header__BZXOb')
    DATE_INPUT = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    RENTAL_DURATION_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_DURATION_LIST = (By.CLASS_NAME, 'Dropdown-menu')
    DROPDOWN_ITEM_RENTAL_PERIOD = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='двое суток']")
    CHECKBOX_BLACK = (By.ID, 'black')
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    POP_UP_CONFIRM_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')

    YES_POP_BUTTON = (By.XPATH, '//button[text()="Да"]')

    COMPLETE_ORDER_POP_UP = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')


