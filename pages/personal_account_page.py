import allure

from data import UserData
from locators.locators import PersonalAccountPageLocators, LoginPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step("Ждем открытия страницы пользователя")
    def wait_for_profile_page(self):
        self.wait_for_element_presence(PersonalAccountPageLocators.LOG_OUT_BUTTON)

    @allure.step("Вводим почту в поле email")
    def enter_email(self, email=UserData.EMAIL):
        self.find_and_click_element(LoginPageLocators.EMAIL).send_keys(email)

    @allure.step("Вводим пароль в поле пароль")
    def enter_password(self, password=UserData.PASSWORD):
        self.find_and_click_element(LoginPageLocators.PASSWORD).send_keys(password)

    @allure.step("Авторизация")
    def login(self, data):
        email, password, name = data
        self.wait_for_element_presence(LoginPageLocators.LOGIN)
        self.enter_email(email)
        self.enter_password(password)
        self.find_and_click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Кликаем по кнопке Выход из аккаунта")
    def log_out_personal_account(self):
        self.click_on_element(PersonalAccountPageLocators.LOG_OUT_BUTTON)

    @allure.step("Кликаем по кнопке История заказов")
    def click_order_history_button(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

