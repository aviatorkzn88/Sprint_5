import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import TestLocators
from urls import Urls
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import user_reg_helper


class TestRegistration:

    def test_registration_form_success_user_data_correct(self, driver: WebDriver, user_data: dict[str, str]):
        driver.get(Urls.BASE_URL)

        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_REGISTER)).click()

        user_reg_helper(driver, user_data['name'], user_data['email'], user_data['password'])

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        assert "/login" in driver.current_url

    def test_registration_form_error_user_password_incorrect(self, driver: WebDriver, user_data: dict[str, str]):
    
        driver.get(Urls.BASE_URL)

        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_REGISTER)).click()

        user_reg_helper(driver, user_data['name'], user_data['email'], 'pass')

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.INVALID_PASSWORD_ERROR))

        