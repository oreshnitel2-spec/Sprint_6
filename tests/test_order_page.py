from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium import webdriver
from data.urls import BASE_URL
from data.parametrize_data import DATA_FOR_ORDER
import pytest
import allure

class TestOrderPage:

    driver = None
    
    
    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @allure.feature("Оформление заказа")
    @allure.story("Проверка успешного оформления заказа с различными данными") 
    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone_number, date, rental_period, color", DATA_FOR_ORDER)
    def test_order_success(self, first_name, last_name, address, metro_station, phone_number, date, rental_period, color):
        self.driver.get(BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_upper_order_button()
        order_page = OrderPage(self.driver)
        order_page.fill_first_page(first_name, last_name, address, metro_station, phone_number)
        order_page.click_next_button()
        order_page.wait_second_page()
        order_page.fill_second_page(date, rental_period, color)
        order_page.click_order_button()
        order_page.wait_order_confirmation()
        order_page.confirm_order()
        success_message = order_page.wait_order_success_message()
        assert "Заказ оформлен" in success_message, f"Ожидали сообщение 'Заказ оформлен', получили {success_message}"
        
          
    @classmethod
    def teardown_class(cls):
        with allure.step("Закрываем браузер Firefox"):
            cls.driver.quit()