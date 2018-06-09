from selenium import webdriver
from selenium .webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from pages.all_incidents import AllIncidentsPage
import pages.all_incidents

class NewTicket():
    def __init__(self, driver):
        self.driver = driver
        # self.frame = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "gsft_main")))
        # self.driver.switch_to.frame(self.frame)
        self.requestedby_field = self.driver.find_element(By.ID, "sys_display.sn_si_incident.caller")
        self.configuration_item_field = self.driver.find_element(By.ID, "sys_display.sn_si_incident.cmdb_ci")
        self.affected_user_field = self.driver.find_element(By.ID, "sys_display.sn_si_incident.affected_user")
        self.location_field = self.driver.find_element(By.ID, "sys_display.sn_si_incident.location")
        self.category_select = Select(self.driver.find_element(By.ID, "sn_si_incident.category"))
        self.subcategory_select = Select(self.driver.find_element(By.ID, "sn_si_incident.subcategory"))
        self.state_select = Select(self.driver.find_element(By.ID, "sn_si_incident.state"))
        self.substate_select = Select(self.driver.find_element(By.ID, "sn_si_incident.substate"))
        self.source_select = Select(self.driver.find_element(By.ID, "sn_si_incident.contact_type"))
        self.business_critical_select = Select(self.driver.find_element(By.ID, "sn_si_incident.business_criticality"))
        self.priority_select = Select(self.driver.find_element(By.ID, "sn_si_incident.priority"))
        self.assignment_group_field = self.driver.find_element(By.ID, "sys_display.sn_si_incident.assignment_group")
        self.assign_to_field = self.driver.find_element(By.ID, "sys_display.sn_si_incident.assigned_to")
        self.short_description_field = self.driver.find_element(By.ID, "sn_si_incident.short_description")
        self.description_field = self.driver.find_element(By.ID, "sn_si_incident.description")
        self.additional_comment_field = self.driver.find_element(By.ID, "sn_si_incident.comments")
        self.work_notes_field = self.driver.find_element(By.ID, "sn_si_incident.work_notes")
        self.secure_notes_field = self.driver.find_element(By.ID, "sn_si_incident.secure_notes")
        self.source_ip_field = self.driver.find_element(By.ID, "sn_si_incident.source_ip")
        self.destination_ip_field = self.driver.find_element(By.ID, "sn_si_incident.dest_ip")
        self.malware_hash_field = self.driver.find_element(By.ID, "sn_si_incident.malware_hash")
        self.other_ioc_field = self.driver.find_element(By.ID, "sn_si_incident.other_ioc")
        self.malware_url_field = self.driver.find_element(By.ID, "sn_si_incident.malware_url")
        self.referrer_url_field = self.driver.find_element(By.ID, "sn_si_incident.referrer_url")
        self.submit_button = self.driver.find_element(By.ID, "sysverb_insert")


    def set_category(self, value):
        self.category_select.select_by_visible_text(value)

    def set_subcategory(self, value):
        self.subcategory_select.select_by_visible_text(value)

    def set_state(self, value):
        self.state_select.select_by_visible_text(value)

    def set_substate(self, value):
        self.substate_select.select_by_visible_text(value)

    def set_source(self, value):
        self.source_select.select_by_visible_text(value)

    def set_business_critical(self, value):
        self.business_critical_select.select_by_visible_text(value)

    def set_priority(self, value):
        self.priority_select.select_by_visible_text(value)

    def set_requested_by(self, value):
        self.requestedby_field.send_keys(value)

    def set_configuration_item(self, value):
        self.configuration_item_field.send_keys(value)

    def set_affected_user(self, value):
        self.affected_user_field.send_keys(value)

    def set_location(self, value):
        self.location_field.send_keys(value)

    def set_assignment_group(self, value):
        self.assignment_group_field.send_keys(value)

    def set_assign_to(self, value):
        self.assign_to_field.send_keys(value)

    def set_short_description(self, value):
        self.short_description_field.send_keys(value)

    def set_description(self, value):
        self.description_field.send_keys(value)

    def set_additional_comment(self, value):
        self.additional_comment_field.send_keys(value)

    def set_work_notes(self, value):
        self.work_notes_field.send_keys(value)

    def set_secure_notes(self, value):
        self.secure_notes_field.send_keys(value)

    def set_source_ip(self, value):
        self.source_ip_field.send_keys(value)

    def set_destination_ip(self, value):
        self.destination_ip_field.send_keys(value)

    def set_malware_hash(self, value):
        self.malware_hash_field.send_keys(value)

    def set_other_ioc(self, value):
        self.other_ioc_field.send_keys(value)

    def set_malware_url(self, value):
        self.malware_url_field.send_keys(value)

    def set_referrer_url(self, value):
        self.referrer_url_field.send_keys(value)

    def click_submit_button(self):
        self.submit_button.click()
        self.driver.switch_to.default_content()
        return pages.all_incidents.AllIncidentsPage(self.driver)

