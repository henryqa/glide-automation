from selenium import webdriver
from selenium .webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AllIncidentsPage():
    def __init__(self, driver):
        self.driver = driver
        self.frame = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "gsft_main")))
        self.driver.switch_to.frame(self.frame)
        self.new_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "sysverb_new")))
        self.total_rows = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                "//nav[@id='list_nav_sn_si_incident']//div[@class='vcr_controls']//span[contains(@id, 'total_rows')]")))


    def click_new_button(self):
        self.new_button.click()

    def get_total_rows(self):
        return self.total_rows.text