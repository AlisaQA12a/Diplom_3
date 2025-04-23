import allure

from selenium import webdriver
from seletools.actions import drag_and_drop
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import (
    MainPageLocators,
    PersonalAccountPageLocators,
    LoginPageLocators,
    OrderPageLocators,
    RecoveryPasswordLocators,
)
from data import Settings


class StellarBurgersTestcase:
    main_page = MainPageLocators()
    login_page = LoginPageLocators()
    order_page = OrderPageLocators()
    account_page = PersonalAccountPageLocators()
    recovery_password = RecoveryPasswordLocators()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем сайт")
    def open_site(self, url):
        self.driver.get(url)

    @allure.step("Находим элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Находим элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Находим и кликаем по элементу")
    def find_and_click_element(self, locator):
        self.wait_for_element_presence(locator)
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        return element

    @allure.step("Кликаем по элементу")
    def click_on_element(self, locator, timeout=Settings.global_timeout):
        element = self.wait_until_visible(locator, timeout)

        if isinstance(self.driver, webdriver.Chrome):
            element.click()
        elif isinstance(self.driver, webdriver.Firefox):
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
        else:
            raise RuntimeError("unsupported webdriver")
        return element

    @allure.step("Ждем пока элемент  станет невидимым")
    def wait_until_element_hide(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Ждем пока элемент станет видимым")
    def wait_until_visible(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, locator, timeout=Settings.global_timeout):
        element = self.wait_until_visible(locator, timeout)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ждем пока элемен станет кликабельным")
    def wait_until_clickable(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ждем загрузку сраницы")
    def wait_until_page_load(self, url, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step("Ждем появления элемента")
    def wait_for_element_presence(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ждем пока элемент станет видимым и кликабельным")
    def wait_until_element_clickable(self, locator, time=Settings.global_timeout):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    @allure.step("Получаем текущую ссылку")
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step("Получаем текст элемента")
    def get_text_of_element(self, locator, timeout=Settings.global_timeout):
        element = self.wait_until_visible(locator, timeout)
        return element.text

    @allure.step("Ждем невидимости элемента")
    def wait_invisibility_of_element(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop_element(self, sourse, target):
        source_element = self.driver.find_element(*sourse)
        target_element = self.driver.find_element(*target)
        drag_and_drop(self.driver, source_element, target_element)

    @allure.step("Кликаем на элемент, перекрытый другим элементом выше по z-index")
    def click_overlapped(self, locator):
        element = self.wait_for_element_presence(locator)
        return self.driver.execute_script("arguments[0].click();", element)