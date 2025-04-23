import allure

from locators.locators import OrderPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):
    @allure.step('Ждем открытия страницы "Лента заказов"')
    def wait_for_page_open(self):
        return self.wait_for_element_presence(OrderPageLocators.HEADER_ORDER_LIST)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        self.wait_for_element_presence(OrderPageLocators.ORDER_NUMBER_IN_HISTORY)
        elements = self.find_elements(OrderPageLocators.ORDER_NUMBER_IN_HISTORY)
        return [element.text for element in elements]


    @allure.step('Получаем значение счетчика "Выполнено за сегодня"')
    def get_number_of_orders_today(self):
        number = self.wait_for_element_presence(OrderPageLocators.TODAY_ORDER_COUNTER)
        return int(number.text)

    @allure.step('Ожидаем значение счетчика "Выполнено за сегодня" отличное от прошлого')
    def wait_numbers_of_orders_today_different(self, value):
        self.wait_for_element_presence(OrderPageLocators.TODAY_ORDER_COUNTER)
        by, loc = OrderPageLocators.TODAY_ORDER_COUNTER_VALUE
        loc = loc.format(value)
        locator = by, loc
        self.wait_until_element_hide(locator)
        element = self.find_element(OrderPageLocators.TODAY_ORDER_COUNTER)
        return int(element.text)

    @allure.step("Проверяем идентификатор заказа в ленте заказов")
    def find_order_number_in_orders_list(self, order_nums):
        self.wait_for_element_presence(OrderPageLocators.ORDERS_HISTORY)
        elements = self.find_elements(OrderPageLocators.ORDERS_HISTORY)
        order_nums_in_orders_list = [element.text for element in elements]
        return all(ORDER_NUMBER in order_nums_in_orders_list for ORDER_NUMBER in order_nums)

    @allure.step("Открываем карточку заказа кликом по ней")
    def click_and_open_order_card(self):
        self.wait_until_visible(OrderPageLocators.ORDER_CARD).click()

    @allure.step("Получаем количества заказов")
    def get_all_orders_counter(self):
        return self.get_text_of_element(OrderPageLocators.TOTAL_ORDER_COUNTER)

    @allure.step("Ждем количество заказов не равное старому значению")
    def wait_all_orders_counter_different(self, value):
        self.wait_for_element_presence(OrderPageLocators.TOTAL_ORDER_COUNTER)
        by, loc = OrderPageLocators.TOTAL_ORDER_COUNTER_VALUE
        loc = loc.format(value)
        locator = by, loc
        self.wait_until_element_hide(locator)
        return self.get_text_of_element(OrderPageLocators.TOTAL_ORDER_COUNTER)

    @allure.step("Ждем появления состава")
    def get_structure_presence(self):
        return self.wait_for_element_presence(OrderPageLocators.ORDER_STRUCTURE)

    @allure.step('Ожидаем появления заказа в "В работе"')
    def wait_for_order_in_work(self, order_number):
        by, loc = OrderPageLocators.ORDER_IN_WORK_BY_NUMBER
        loc = loc.format(order_number.lstrip("0"))
        locator = (by, loc)
        return self.wait_for_element_presence(locator)