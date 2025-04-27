import allure
import pytest
import requests

from selenium import webdriver
from helpers import generate_user_data
from url import Urls

from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


@allure.step("Создание драйвера")
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise RuntimeError("Неподдерживаемый браузер")
    driver.set_window_size(1920, 1080)
    driver.get(Urls.MAIN_URL)
    yield driver
    driver.quit()


@allure.step("Создание и удаление пользователя")
@pytest.fixture(scope="session")
def user_auth_data():
    email, password, name = generate_user_data()
    params = {
        "email": email,
        "password": password,
        "name": name,
    }
    response = requests.post(Urls.CREATE_USER_API, data=params)
    data = response.json()
    user_data = [email, password, name]

    yield user_data, response.json()

    auth_token = data.get("accessToken")
    headers = {"Authorization": f"{auth_token}"}
    requests.delete(Urls.DELETE_USER_API, headers=headers)


@allure.step("Использование динамического пользователя")
@pytest.fixture(scope="session")
def user_data(user_auth_data):
    data, _ = user_auth_data
    return data


@allure.step("Аутентификация под пользователем")
@pytest.fixture
def login(driver, user_data):
    main_page = MainPage(driver)
    main_page.click_and_go_to_personal_account()
    personal_account_page = PersonalAccountPage(driver)
    personal_account_page.login(user_data)
    main_page.main_page_loading_wait()
    return user_data