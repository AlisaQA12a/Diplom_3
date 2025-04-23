import allure

from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderListPage:
    @allure.title("Проверяем появление всплывающего окна с деталями по клику на заказ")
    def test_open_order_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_and_go_to_order_list_page()
        order_list_page = OrderListPage(driver)
        order_list_page.click_and_open_order_card()
        assert order_list_page.get_structure_presence()

    @allure.title('Проверяем отображение заказов из раздела "История заказов" на странице "Лента заказов"')
    def test_order_history_is_in_order_list(self, driver, login):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        main_page.drag_and_drop_bun()
        main_page.order()

        main_page.click_and_go_to_personal_account()
        personal_account_page.wait_for_profile_page()
        personal_account_page.click_order_history_button()
        order_nums = order_list_page.get_order_number()

        main_page.click_and_go_to_order_list_page()
        assert order_list_page.find_order_number_in_orders_list(order_nums)

    @allure.title('Проверяем увеличение счетчика "Выполнено за всё время" при создании нового заказа')
    def test_when_create_order_counter_increases_for_all_time(self, driver, login):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_and_go_to_order_list_page()
        order_list_page.wait_for_page_open()
        order_counter = order_list_page.get_all_orders_counter()

        main_page.open_constructor()
        main_page.drag_and_drop_bun()
        main_page.order()

        main_page.click_and_go_to_order_list_page()
        order_list_page.wait_for_page_open()
        order_counter2 = order_list_page.wait_all_orders_counter_different(order_counter)

        assert int(order_counter) < int(order_counter2)

    @allure.title('Проверяем увеличение счётчика "Выполнено за сегодня" при создании нового заказа')
    def test_when_create_order_today_counter_increases(self, driver, login):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_and_go_to_order_list_page()
        order_list_page.wait_for_page_open()
        order_counter = order_list_page.get_number_of_orders_today()

        main_page.open_constructor()
        main_page.drag_and_drop_bun()
        main_page.order()
        main_page.click_and_go_to_order_list_page()
        order_list_page.wait_for_page_open()
        order_counter2 = order_list_page.wait_numbers_of_orders_today_different(order_counter)

        assert order_counter < order_counter2

    @allure.title("Проверяем появление номера заказа в разделе 'В работе' после оформления заказа")
    def test_order_listed_in_work(self, driver, login):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        main_page.drag_and_drop_bun()
        order_number = main_page.order()
        main_page.click_and_go_to_order_list_page()
        order_list_page.wait_for_page_open()
        assert order_list_page.wait_for_order_in_work(order_number)