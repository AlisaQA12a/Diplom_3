class Urls:
    MAIN_URL = "https://stellarburgers.nomoreparties.site"
    LOGIN = MAIN_URL + "/login"
    ORDER_HISTORY_URL = MAIN_URL + "/account/order-history"
    ORDER_LIST_URL = MAIN_URL + "/feed"
    PROFILE_URL = MAIN_URL + "/account/profile"  # ссылка на личный кабинет

    FORGOT_PASSWORD_URL = MAIN_URL + "/forgot-password"  # ссылка на страницу ввода email для восстановления пароля
    RESET_PASSWORD_URL = MAIN_URL + "/reset-password"  # ссылка на страницу ввода нового пароля и кода из письма

    
    CREATE_USER_API = MAIN_URL + "/api/auth/register"  # POST создание пользователя
    DELETE_USER_API = MAIN_URL + "/api/auth/user"  # DELETE удаление пользователя