from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.all_incidents


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.all_tickets_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                      "//div[@id='edge_pinned_bookmarks']/div[./button/span[contains(., 'Security Incident - Show All Incidents')]]")))

    def click_security_incident_all_button(self):
        self.all_tickets_button.click()
        return pages.all_incidents.AllIncidentsPage(self.driver)
