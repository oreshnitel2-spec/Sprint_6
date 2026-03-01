from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step("Заполняем имя: {first_name}")
    def fill_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME).send_keys(first_name)

    @allure.step("Заполняем фамилию: {last_name}")
    def fill_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.LAST_NAME).send_keys(last_name)

    @allure.step("Заполняем адрес: {address}")
    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS).send_keys(address)

    @allure.step("Заполняем станцию метро: {metro_station}")
    def fill_metro_station(self, metro_station):
        self.driver.find_element(*OrderPageLocators.METRO_STATION).send_keys(metro_station)
        metro_option = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//div[text()='{metro_station}']")))
        metro_option.click()

    @allure.step("Заполняем номер телефона: {phone_number}")
    def fill_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER).send_keys(phone_number)

    @allure.step("Ожидаем загрузки второй страницы заказа")
    def wait_second_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.DATE_PICKER))

    @allure.step("Заполняем дату доставки: {date}")
    def fill_date(self, date):
        date_input = self.driver.find_element(*OrderPageLocators.DATE_PICKER)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбираем период аренды: {period}")
    def select_rental_period(self, period):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        period_option = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//div[text()='{period}']")))
        period_option.click()

    @allure.step("Выбираем цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.driver.find_element(*OrderPageLocators.BLACK_COLOR_CHECKBOX).click()
        elif color == "grey":
            self.driver.find_element(*OrderPageLocators.GREY_COLOR_CHECKBOX).click()
        else:
            raise ValueError(f"Unknown color: {color}")
        
    @allure.step("Клик по кнопке 'Заказать'")
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    @allure.step("Ожидаем появления окна подтверждения заказа")
    def wait_order_confirmation(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.YES_BUTTON))

    @allure.step("Кликаем на кнопку 'Да' в окне подтверждения заказа")
    def confirm_order(self):
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    @allure.step("Ожидаем появления сообщения об успешном оформлении заказа")
    def wait_order_success_message(self):
        message = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_MESSAGE))
        return message.text
    
    def fill_first_page(self, first_name, last_name, address, metro_station, phone_number):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.fill_metro_station(metro_station)
        self.fill_phone_number(phone_number)

    def fill_second_page(self, date, rental_period, color):
        self.fill_date(date)
        self.select_rental_period(rental_period)
        self.select_color(color)

    