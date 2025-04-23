import allure

from locators.locators import MainPageLocators
from pages.main_page import MainPage
from url import Urls


class TestCheckMainPage:
    @allure.title('Проверяем успешный переход по клику на  "Лента заказов"')
    def test_click_on_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_and_go_to_order_list_page()
        assert main_page.wait_until_page_load(Urls.ORDER_LIST_URL)

    @allure.title('Проверяем успешный переход по клику на "Конструктор"')
    def test_click_on_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_and_go_to_order_list_page()
        main_page.open_constructor()
        assert main_page.wait_until_page_load(Urls.MAIN_URL)

    @allure.title("Проверяем появление окна с деталями по клику на ингредиент")
    def test_check_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient()
        text = main_page.popup_with_ingredient_details()
        assert text == "Детали ингредиента"

    @allure.title("Проверяем что всплывающее окно закрывается по клику на крестик")
    def test_check_close_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient()
        main_page.popup_with_ingredient_details()
        main_page.close_popup()
        assert main_page.ingredient_popup_is_invisible()

    @allure.title("Проверяем увеличение счетчика ингридиента при добавлении его в заказ")
    def test_change_counter_when_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        count = main_page.get_count_ingredients()
        main_page.drag_and_drop_bun()
        new_count = main_page.wait_count_ingredients_is_valuable("2")
        assert count == "0" and new_count == "2"

    @allure.title("Проверяем что авторизованный пользователь может оформить заказ")
    def test_create_order_with_authorized_user(self, driver, login):
        main_page = MainPage(driver)
        main_page.drag_and_drop_bun()
        main_page.find_and_click_order_button()
        assert main_page.get_text_of_element(MainPageLocators.POPUP_ORDER_STATUS) == "Ваш заказ начали готовить"