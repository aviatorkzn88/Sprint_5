from selenium.webdriver.common.by import By

class TestLocators:
    # Главная страница
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']") # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # Логотип сервиса
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']") # Кнопка "Личный кабинет"
    CREATE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"

    # Конструктор
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div") # Вкладка "Булки"
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div") # Вкладка "Соусы"
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div") # Вкладка "НАчинки"

    # Форма входа/регистрации
    NAME_INPUT = (By.XPATH, ".//div[div/label[text()='Имя']]//input") # Поле ввода "Имя"
    EMAIL_INPUT = (By.XPATH, ".//div[div/label[text()='Email']]//input") # Поле ввода "Email"
    PASSWORD_INPUT = (By.XPATH, ".//div[div/label[text()='Пароль']]//input") # Поле ввода "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти"
    
    # Ссылки в формах
    LINK_TO_REGISTER = (By.XPATH, ".//a[@href='/register']") # Ссылка "Зарегистрироваться" в форме "Вход"
    LINK_TO_LOGIN = (By.XPATH, ".//a[@href='/login']") # Ссылка "Войти" в форме "Регистрация"
    LINK_TO_FORGOT_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']") # ссылка "Восстановить пароль" в форме "Вход"
    
    # Личный кабинет
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выход"

    
    # Ошибки
    INVALID_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']") # Сообщение об ошибке "Некорректный пароль"
