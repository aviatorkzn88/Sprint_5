from selenium.webdriver.common.by import By

class TestLocators:
    # Главная страница
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # Секции конструктора
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    # Активная вкладка в конструкторе (для проверки перехода)
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]")

    # Форма входа/регистрации
    NAME_INPUT = (By.XPATH, ".//div[div/label[text()='Имя']]//input")
    EMAIL_INPUT = (By.XPATH, ".//div[div/label[text()='Email']]//input")
    PASSWORD_INPUT = (By.XPATH, ".//div[div/label[text()='Пароль']]//input")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    
    # Ссылки в формах
    LINK_TO_REGISTER = (By.XPATH, ".//a[@href='/register']")
    LINK_TO_LOGIN = (By.XPATH, ".//a[@href='/login']")
    LINK_TO_FORGOT_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")
    
    # Личный кабинет
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    
    # Ошибки
    INVALID_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")
