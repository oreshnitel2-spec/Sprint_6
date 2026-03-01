from selenium.webdriver.common.by import By

class MainPageLocators:
    UPPER_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    LOWER_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")

    @staticmethod
    def faq_question_locator(index):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def faq_answer_locator(index):
        return (By.ID, f"accordion__panel-{index}")