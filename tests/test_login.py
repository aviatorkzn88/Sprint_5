import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import user_log_helper


class TestLogin:

    def test_login_by_login_button_from_main_page_success(self, driver: WebDriver, registered_user: dict[str, str]):

        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        user_log_helper(driver, registered_user['email'], registered_user['password'])

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER))
        

    def test_login_by_profile_button_from_main_page_success(self, driver: WebDriver, registered_user: dict[str, str]):

        driver.find_element(*TestLocators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        user_log_helper(driver, registered_user['email'], registered_user['password'])

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER))
        

    def test_login_by_login_link_from_registration_form_success(self, driver: WebDriver, registered_user: dict[str, str]):

        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_REGISTER)).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_LOGIN)).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        user_log_helper(driver, registered_user['email'], registered_user['password'])

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER))
 
    def test_login_by_link_to_forgot_password_from_login_form_success(self, driver: WebDriver, registered_user: dict[str, str]):

        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_FORGOT_PASSWORD)).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LINK_TO_LOGIN)).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        user_log_helper(driver, registered_user['email'], registered_user['password'])

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER))
        