from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_MAIN_PAGE = (By.XPATH, ".//p[text()='Личный Кабинет']")  # личный кабинет на главной странице
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__')]/parent::div")
    ORDER_LIST = (By.XPATH, "//p[text()='Лента Заказов']")
    MAIN_PAGE_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    POPUP_INGREDIENT_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENTS_COUNTER = (
        By.XPATH,
        (
            '//h2[text() = "Булки"]/following-sibling::ul[1]/*/'
            'p[text()="Флюоресцентная булка R2-D3"]/parent::a/*/'
            'p[contains(@class, "counter_counter__num__")]'
        )
    )
    INGREDIENT_COUNTER_VALUE = (
        By.XPATH,
        (
            '//h2[text() = "Булки"]/following-sibling::ul[1]/*/'
            'p[text()="Флюоресцентная булка R2-D3"]/parent::a/*/'
            'p[contains(@class, "counter_counter__num__") and text() = "{}"]'
        )
    )  # Счетчик (поиск по заданному количеству)
    STORE_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    POPUP_ORDER_STATUS = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')  # Ваш заказ начали готовить в попапе
    MODAL_BACKDROP_OPENED = (By.XPATH, "(//section[contains(@class,'Modal_modal_opened__')])")
    ORDER_MODAL_LOADER = (By.XPATH, "(//div[contains(@class,'Modal_modal_opened__')])")
    ORDER_MODAL_NUMBER_INVALID = (
        By.XPATH,
        (
            "//h2[contains(@class, 'Modal_modal__title_shadow__')"
            " and contains(@class, 'text_type_digits-large')"
            " and text() = '9999']"
        ),
    )
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title_shadow__') and contains(@class, 'text_type_digits-large')]",
    )
    ORDER_PRICE = (
        By.XPATH,
        (
            "//div[contains(@class, 'BurgerConstructor_basket__totalContainer__')]"
            "//p[contains(@class, 'text_type_digits') and text() != '0']"
        ),
    )

class LoginPageLocators:
        LOGIN = (By.XPATH, ".//h2[text()='Вход']")  # заголовок Вход
        EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input[1]")
        PASSWORD = (By.NAME, "Пароль")
        LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

        INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода почты
        INPUT_PASSWORD_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")  # активное поле пароля
        LINK_TO_ENTER = (By.CSS_SELECTOR, 'a[href="/login"]')  # ссылка Войти

class PersonalAccountPageLocators:
        LOG_OUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
        SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
        PROFILE_BUTTON = (By.LINK_TEXT, "Профиль")
        ORDER_HISTORY_BUTTON = (By.LINK_TEXT, "История заказов")

class OrderPageLocators:
        HEADER_ORDER_LIST = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок "Лента заказов"
        ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'  # Состав
        ORDER_CARD = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__')])[2]")
        ORDERS_HISTORY = (
            By.XPATH,
            "//div[contains(@class, 'OrderHistory_textBox__')]/p[contains(@class, 'text_type_digits-default')]",
        )
        ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
        TOTAL_ORDER_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
        TOTAL_ORDER_COUNTER_VALUE = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[text() = '{}']")
        TODAY_ORDER_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
        TODAY_ORDER_COUNTER_VALUE = (
        By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[text() = '{}']")
        NUMBER_IN_WORK = (
        By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")  # Номер "В работе"
        ORDER_IN_WORK_BY_NUMBER = (
            By.XPATH,
            (
                "//div[contains(@class, 'OrderFeed_orderStatusBox__')]"
                "//ul[contains(@class, 'OrderFeed_orderListReady__')]"
                "//li[contains(@class, 'text_type_digits-default') and text() = '{}']"
            ),
        )

class RecoveryPasswordLocators:
        RESET_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
        FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')
        INPUT_NEW_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")
        VISIBLE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")  # кнопка показать пароль