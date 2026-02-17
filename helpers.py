import random
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


def generate_user_data():
    name = "Timur"
    last_name = "Sharipov"
    cohort = "39"
    random_id = random.randint(100, 999)
    email = f"{name}.{last_name}.{cohort}.{random_id}@yandex.ru"
    return {
        'name': name,
        'email': email, 
        'password': 'password123'
    }

def user_log_helper(driver, email, password):
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()

def user_reg_helper(driver, name, email, password):
    driver.find_element(*TestLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*TestLocators.REGISTER_BUTTON).click()