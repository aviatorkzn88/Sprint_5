import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_form_success_user_data_correct(self, driver: WebDriver, user_data: dict[str, str]):
        driver.get("https://stellarburgers.education-services.ru/")

        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_REGISTER)).click()

        driver.find_element(*TestLocators.NAME_INPUT).send_keys(user_data['name'])
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user_data['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(user_data['password'])
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        assert "/login" in driver.current_url

        driver.quit()

    def test_registration_form_error_user_password_incorrect(self, driver: WebDriver, user_data: dict[str, str]):
    
        driver.get("https://stellarburgers.education-services.ru/")

        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_REGISTER)).click()

        driver.find_element(*TestLocators.NAME_INPUT).send_keys(user_data['name'])
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user_data['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.INVALID_PASSWORD_ERROR))

        assert "Некорректный пароль" in error_message.text

        driver.quit()
        

     

