import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:

    def test_switch_to_buns_section_success(self, driver: WebDriver):
        driver.get("https://stellarburgers.education-services.ru/")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SAUCES_SECTION)).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.BUNS_SECTION)).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute(TestLocators.BUNS_SECTION, 'class', 'tab_tab_type_current'))

        target_attribute = driver.find_element(*TestLocators.BUNS_SECTION).get_attribute("class") or ""

        assert 'tab_tab_type_current' in target_attribute

        driver.quit()

    def test_switch_to_sauses_section_success(self, driver: WebDriver):
        driver.get("https://stellarburgers.education-services.ru/")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SAUCES_SECTION)).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute(TestLocators.SAUCES_SECTION, 'class', 'tab_tab_type_current'))

        target_attribute = driver.find_element(*TestLocators.SAUCES_SECTION).get_attribute("class") or ""

        assert 'tab_tab_type_current' in target_attribute

        driver.quit()

    def test_switch_to_fillings_section_success(self, driver: WebDriver):
        driver.get("https://stellarburgers.education-services.ru/")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.FILLINGS_SECTION)).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute(TestLocators.FILLINGS_SECTION, 'class', 'tab_tab_type_current'))

        target_attribute = driver.find_element(*TestLocators.FILLINGS_SECTION).get_attribute("class") or ""

        assert 'tab_tab_type_current' in target_attribute

        driver.quit()  
