from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from locators.main_page_locators import MainPageLocators
import allure

class MainPage:
    

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_upper_order_button(self):
        self.driver.find_element(*MainPageLocators.UPPER_ORDER_BUTTON).click()

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_lower_order_button(self):
        lower_order_button = self.driver.find_element(*MainPageLocators.LOWER_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", lower_order_button)
        self.driver.execute_script("arguments[0].click();", lower_order_button)

    @allure.step("Кликаем на вопрос FAQ с индексом {index}")
    def click_faq_question(self, index):
        question_locator = MainPageLocators.faq_question_locator(index)
        question = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(question_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", question)
        self.driver.execute_script("arguments[0].click();", question)

    @allure.step("Получаем текст ответа на вопрос FAQ с индексом {index}")
    def get_faq_answer_text(self, index):
        answer_locator = MainPageLocators.faq_answer_locator(index)
        answer = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(answer_locator))
        return answer.text