import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestProfile:

    def test_go_to_profile_by_profile_button_from_main_page_success(self, driver: WebDriver, login_user: None):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/account/profile'

        driver.quit()

    def test_go_to_constructor_by_constructor_button_from_profile_success(self, driver: WebDriver, login_user: None):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/'

        driver.quit()

    def test_go_to_constructor_by_logo_button_from_profile_success(self, driver: WebDriver, login_user: None):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

        driver.find_element(*TestLocators.LOGO_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/'

        driver.quit()

    def test_logout_by_logout_button_from_profile_success(self, driver: WebDriver, login_user: None):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

        driver.quit() 
                    