import allure

from locators.locators import MainPageLocators
from pages.base_page import BasePage
from url import Urls


class MainPage(BasePage):
    @allure.step("Открываем сайт")
    def open_main_page(self):
        return self.open_site(Urls.MAIN_URL)

    @allure.step("Ждем загрузку страницы")
    def main_page_loading_wait(self):
        return self.wait_until_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Переходим в личный кабинет")
    def click_and_go_to_personal_account(self):
        return self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_MAIN_PAGE)

    @allure.step("Переходим на страницу Лента заказов")
    def click_and_go_to_order_list_page(self):
        return self.click_on_element(MainPageLocators.ORDER_LIST)

    @allure.step("Переходим по клику в конструктор")
    def open_constructor(self):
        self.click_on_element(MainPageLocators.MAIN_PAGE_CONSTRUCTOR)
        return self.wait_until_visible(MainPageLocators.MAIN_PAGE_CONSTRUCTOR)

    @allure.step("Кликаем по инредиенту")
    def click_on_ingredient(self):
        self.wait_until_clickable(MainPageLocators.BUN_INGREDIENT)
        return self.click_on_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step('Ждем появления попапа "Детали ингредиента"')
    def popup_with_ingredient_details(self):
        self.wait_until_visible(MainPageLocators.POPUP_INGREDIENT_DETAILS)
        return self.get_text_of_element(MainPageLocators.POPUP_INGREDIENT_DETAILS)

    @allure.step("Закрываем попап кликом на крестик")
    def close_popup(self):
        return self.click_overlapped(MainPageLocators.CLOSE_BUTTON)

    @allure.step("Ждем пока появится попап с номером заказа")
    def wait_for_order_popup(self):
        return self.wait_for_element_presence(MainPageLocators.POPUP_ORDER_STATUS)

    @allure.step("Ждем лоадер в попапе с номером заказа")
    def wait_for_order_loader(self):
        return self.wait_for_element_presence(MainPageLocators.ORDER_MODAL_LOADER)

    @allure.step("Ждем скрытия лоадера в попапе с номером заказа")
    def wait_for_order_loader_hide(self):
        return self.wait_until_element_hide(MainPageLocators.ORDER_MODAL_LOADER)

    @allure.step("Проверяем, что попап с заказом невидим")
    def order_popup_is_invisible(self):
        return self.wait_invisibility_of_element(MainPageLocators.POPUP_ORDER_STATUS)

    @allure.step("Проверяем, что попап с деталями ингридиента невидим")
    def ingredient_popup_is_invisible(self):
        return self.wait_invisibility_of_element(MainPageLocators.POPUP_INGREDIENT_DETAILS)

    @allure.step("Получаем количество ингредиентов из счётчика")
    def get_count_ingredients(self):
        self.wait_for_element_presence(MainPageLocators.INGREDIENTS_COUNTER)
        counter_element = self.find_element(MainPageLocators.INGREDIENTS_COUNTER)
        return counter_element.text

    @allure.step("Ждем, пока количество ингридиентов в счётчике станет равным ожидаемому")
    def wait_count_ingredients_is_valuable(self, count):
        by, loc = MainPageLocators.INGREDIENT_COUNTER_VALUE
        loc = loc.format(count)
        locator = by, loc
        self.wait_for_element_presence(locator)
        counter_element = self.find_element(locator)
        return counter_element.text

    @allure.step("Находим и кликаем по кнопке Оформить заказ")
    def find_and_click_order_button(self):
        return self.find_and_click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Перетаскиваем булку в корзину")
    def drag_and_drop_bun(self):
        self.wait_until_clickable(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.STORE_BASKET)
        return self.wait_for_element_presence(MainPageLocators.ORDER_PRICE)

    @allure.step("Ждем пока глобальный фон попапа перестанет быть открытым")
    def wait_until_backdrop_hide(self):
        return self.wait_until_element_hide(MainPageLocators.MODAL_BACKDROP_OPENED)

    @allure.step("Заказываем, ждем окно заказа и закрываем его")
    def order(self):
        self.find_and_click_order_button()
        self.wait_for_order_popup()
        self.wait_for_element_presence(MainPageLocators.ORDER_MODAL_NUMBER_INVALID)
        self.wait_for_order_loader()
        self.wait_until_element_hide(MainPageLocators.ORDER_MODAL_NUMBER_INVALID)
        self.wait_for_order_loader_hide()
        self.wait_for_element_presence(MainPageLocators.ORDER_MODAL_NUMBER)
        order_number = self.get_text_of_element(MainPageLocators.ORDER_MODAL_NUMBER)
        self.wait_for_order_loader_hide()
        self.close_popup()
        self.order_popup_is_invisible()
        self.wait_until_backdrop_hide()
        return order_number