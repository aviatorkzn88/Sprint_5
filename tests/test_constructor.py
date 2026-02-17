import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import TestLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls


class TestConstructor:

    def test_switch_to_buns_section_success(self, driver: WebDriver):
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SAUCES_SECTION)).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.BUNS_SECTION)).click()

        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute(TestLocators.BUNS_SECTION, 'class', 'tab_tab_type_current'))

    def test_switch_to_sauses_section_success(self, driver: WebDriver):
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SAUCES_SECTION)).click()

        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute(TestLocators.SAUCES_SECTION, 'class', 'tab_tab_type_current'))

    def test_switch_to_fillings_section_success(self, driver: WebDriver):
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.FILLINGS_SECTION)).click()

        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute(TestLocators.FILLINGS_SECTION, 'class', 'tab_tab_type_current'))
        