from selenium import webdriver
from selenium .webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pages.home

class Login():
    def __init__(self, driver):
        self.driver = driver
        self.frame = self.driver.find_element(By.ID, 'gsft_main')
        self.driver.switch_to.frame(self.frame)
        self.username_field = self.driver.find_element(By.ID, 'user_name')
        self.password_field = self.driver.find_element(By.ID, 'user_password')
        self.login_button = self.driver.find_element(By.ID, 'sysverb_login')


    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()
        self.driver.switch_to.default_content()
        return pages.home.HomePage(self.driver)