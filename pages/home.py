from selenium import webdriver
from selenium .webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.all_incidents import AllIncidentsPage

class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def click_security_incident_all_button(self):
        wait = WebDriverWait(self.driver, 30)
        sec_incident_all = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='edge_pinned_bookmarks']/div[./button/span[contains(., 'Security Incident - Show All Incidents')]]")))
        sec_incident_all.click()
        return AllIncidentsPage(self.driver)







