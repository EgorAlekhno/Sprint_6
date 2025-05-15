from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-{}']")
    LAST_QUESTION = (By.XPATH, "//div[@id='accordion__heading-7']")
    ANSWER = (By.XPATH, "//div[@aria-labelledby='accordion__heading-{}']")

    TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    HOW_IT_WORKS_SECTION = (By.XPATH, '//*[contains(text(), "Как это работает")]/ancestor::div[contains(@class, '
                                      '"Home_ThirdPart")]')
    ORDER_BUTTON_IN_HOW_IT_WORKS_SECTION = (By.XPATH, '//*[contains(text(), "Как это работает")]/ancestor::div['
                                                      'contains(@class, "Home_ThirdPart")]//button[text()="Заказать"]')

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
