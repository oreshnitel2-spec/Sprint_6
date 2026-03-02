from pages.main_page import MainPage
from pages.base_page import BasePage
from selenium import webdriver
from data.parametrize_data import FAQ_ANSWERS
from data.urls import BASE_URL
import pytest
import allure


class TestMainPage:

    driver = None

    
    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()


    @allure.feature("FAQ")
    @allure.story("Проверка всех ответов")
    @pytest.mark.parametrize("index, expected_answer", FAQ_ANSWERS)
    def test_faq_answer(self, index, expected_answer):
        self.driver.get(BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_faq_question(index)
        answer_text = main_page.get_faq_answer_text(index)
        assert answer_text == expected_answer, f"Ожидаемый ответ: {expected_answer}, полученный ответ: {answer_text}"

    @allure.feature("Логотипы")
    @allure.story("Проверка клика по Яндекс логотипу")
    def test_yandex_logo_click_success(self):
        self.driver.get(BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_dzen_loaded()
        assert "dzen.ru" in self.driver.current_url, f"Ожидали 'dzen.ru' в URL, получили {self.driver.current_url}"

    @allure.story("Проверка клика по логотипу Самоката")
    def test_samokat_logo_click_success(self):
        self.driver.get(BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_lower_order_button()
        main_page.click_samokat_logo()
        main_page.wait_main_page_loaded()
        assert self.driver.current_url == BASE_URL, f"Ожидали URL '{BASE_URL}', получили {self.driver.current_url}"

    @allure.feature("Заказ")
    @allure.story("Проверка верхней кнопки 'Заказать'")
    def test_upper_order_button_click_success(self):
        self.driver.get(BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_upper_order_button()
        assert "/order" in self.driver.current_url, f"Ожидали URL '{BASE_URL}order', получили {self.driver.current_url}"

    @allure.story("Проверка нижней кнопки 'Заказать'")
    def test_lower_order_button_click_success(self):
        self.driver.get(BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_lower_order_button()
        assert "/order" in self.driver.current_url, f"Ожидали URL '{BASE_URL}order', получили {self.driver.current_url}"

    
    @classmethod
    def teardown_class(cls):
        with allure.step("Закрываем браузер Firefox"):
            cls.driver.quit()