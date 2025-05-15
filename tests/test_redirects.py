import allure
from pages.main_page import MainPage
from data import Urls


class TestLogoRedirects:
    @allure.title("Проверка: переход на главную по клику на логотип 'Самокат'")
    def test_logo_redirects_to_main_page(self, driver):
        driver.get(Urls.ORDER_PAGE)
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        main_page.wait_for_url_to_be(Urls.BASE)
        assert main_page.get_current_url() == Urls.BASE, \
            "Не произошел переход на главную страницу после клика на логотип 'Самокат'"

    @allure.title("Проверка: переход по клику на логотип 'Яндекс' в новой вкладке")
    def test_yandex_logo_opens_in_new_tab(self, driver):
        driver.get(Urls.BASE)
        main_page = MainPage(driver)
        main_page.click_yandex_logo()

        main_page.switch_to_new_tab()
        main_page.wait_for_title_contains("Дзен")

        current_url = main_page.get_current_url()
        assert Urls.YANDEX_REDIRECT in current_url or "yandex" in current_url.lower(), \
            f"Ожидался переход на Яндекс, но открылось: {current_url}"
