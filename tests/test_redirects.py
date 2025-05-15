import allure
from pages.main_page import MainPage


@allure.title("Проверка: переход на главную по клику на логотип 'Самокат'")
def test_logo_redirects_to_main_page(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    main_page = MainPage(driver)
    main_page.click_scooter_logo()
    main_page.wait_for_url_to_be("https://qa-scooter.praktikum-services.ru/")
    assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/", \
        "Не произошел переход на главную страницу после клика на логотип 'Самокат'"


@allure.title("Проверка: переход по клику на логотип 'Яндекс' в новой вкладке")
def test_yandex_logo_opens_in_new_tab(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/")
    main_page = MainPage(driver)
    main_page.click_yandex_logo()

    main_page.switch_to_new_tab()
    main_page.wait_for_title_contains("Дзен")

    current_url = main_page.get_current_url()
    assert "https://dzen.ru/?yredirect=true" in current_url or "yandex" in current_url.lower(), \
        f"Ожидался переход на Яндекс, но открылось: {current_url}"
