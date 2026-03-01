from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.urls import BASE_URL
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    @allure.step("Клик по логотипу Самоката")
    def click_samokat_logo(self):
        self.driver.find_element(*BasePageLocators.SAMOKAT_LOGO).click()

    @allure.step("Ожидаем загрузки страницы Дзена")
    def wait_dzen_loaded(self):
        WebDriverWait(self.driver, 50).until(expected_conditions.url_contains("dzen.ru"))

    @allure.step("Ожидаем загрузки главной страницы")
    def wait_main_page_loaded(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.url_to_be(BASE_URL))