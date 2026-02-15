import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def user_data():
    name = "Timur"
    last_name = "Sharipov"
    cohort = "39"
    random_id = random.randint(100, 999)
    email = f"{name}.{last_name}.{cohort}.{random_id}@yandex.ru"
    return {
        "email": email, 
        "password": "password123", 
        "name": name
    }

@pytest.fixture
def registered_user(driver: WebDriver, user_data: dict[str, str]):
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_REGISTER)).click()

    driver.find_element(*TestLocators.NAME_INPUT).send_keys(user_data['name'])
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user_data['email'])
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(user_data['password'])
    driver.find_element(*TestLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

    driver.find_element(*TestLocators.LOGO_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON_MAIN))

    return user_data

@pytest.fixture
def login_user(driver: WebDriver, registered_user: dict[str, str]):
    driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
    
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER))

    




