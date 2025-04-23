import allure

from pages.recovery_password_page import RecoveryPassword
from url import Urls
from data import UserData


class TestRecoveryPassword:
    @allure.title("Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль» ")
    def test_go_to_the_recovery_password_page_by_button(self, driver):
        recovery_password = RecoveryPassword(driver)
        recovery_password.open_login_page()
        recovery_password.click_recovery_link()

        assert recovery_password.wait_until_page_load(Urls.FORGOT_PASSWORD_URL)

    @allure.title('Проверяем ввод почты и клик по кнопке "Восстановить"')
    def test_input_password_and_click_button_recovery(self, driver):
        recovery_password = RecoveryPassword(driver)
        recovery_password.open_login_page()
        recovery_password.click_recovery_link()
        recovery_password.enter_email_on_recovery_page(UserData.EMAIL)
        recovery_password.click_recovery_btn()

        assert recovery_password.wait_until_page_load(Urls.RESET_PASSWORD_URL)

    @allure.title("Проверяем что клик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_on_visible_password_button(self, driver):
        recovery_password = RecoveryPassword(driver)
        recovery_password.open_login_page()
        recovery_password.click_recovery_link()
        recovery_password.enter_email_on_recovery_page(UserData.EMAIL)
        recovery_password.click_recovery_btn()
        recovery_password.click_on_visible_password_button()
        assert recovery_password.find_active_input_password()