import pytest
from urls import Urls
from helpers import generate_user_data
from helpers import user_log_helper
from helpers import user_reg_helper
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    return generate_user_data()

@pytest.fixture
def registered_user(driver: WebDriver, user_data: dict[str, str]):
    driver.get(Urls.BASE_URL)

    driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_REGISTER)).click()

    user_reg_helper(driver, user_data['name'], user_data['email'], user_data['password'])

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

    driver.find_element(*TestLocators.LOGO_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON_MAIN))

    return user_data

@pytest.fixture
def login_user(driver: WebDriver, registered_user):
    driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
    
    user_log_helper(driver, registered_user['email'], registered_user['password'])

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER))

    return registered_user

    




