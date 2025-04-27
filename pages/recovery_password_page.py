import allure

from locators.locators import LoginPageLocators, RecoveryPasswordLocators
from pages.base_page import BasePage
from url import Urls


class RecoveryPassword(BasePage):
    @allure.step("Открываем страницу авторизации")
    def open_login_page(self):
        self.open_site(Urls.LOGIN)
        return self.wait_for_element_presence(LoginPageLocators.LOGIN)

    @allure.step("Кликаем по ссылке Восстановить пароль")
    def click_recovery_link(self):
        return self.click_on_element(RecoveryPasswordLocators.FORGOT_PASSWORD)

    @allure.step("Кликаем по кнопке Восстановить")
    def click_recovery_btn(self):
        return self.click_on_element(RecoveryPasswordLocators.RESET_BUTTON)

    @allure.step("Вводим почту в поле на странице восстановления пароля")
    def enter_email_on_recovery_page(self, email):
        self.find_and_click_element(LoginPageLocators.INPUT_EMAIL).send_keys(email)

    @allure.step("Кликаем по кнопке Показать/Скрыть пароль")
    def click_on_visible_password_button(self):
        return self.click_on_element(RecoveryPasswordLocators.VISIBLE_PASSWORD_BUTTON)

    @allure.step("Находим активное поле Пароль")
    def find_active_input_password(self):
        return self.wait_until_visible(LoginPageLocators.INPUT_PASSWORD_ACTIVE)

    @allure.step("Вводим новый пароль")
    def enter_new_password(self):
        return self.click_on_element(RecoveryPasswordLocators.INPUT_NEW_PASSWORD)