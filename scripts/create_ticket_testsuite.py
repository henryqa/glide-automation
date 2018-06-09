import unittest, xlrd
from ddt import ddt, data, unpack
import basetestcase
from pages.login import Login


def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows


@ddt
class TicketsTest(basetestcase.BaseTestCase):
    @data(*get_data("../data/create_ticket_testdata.xlsx"))
    @unpack
    def test_create_new_ticket(self, requested_by, configuration_item, affected_user, location, category, subcategory,
                           state, substate, source, business_critical, priority, assignment_group, assigned_to,
                           short_description, description, additional_comment, work_notes, secure_notes, source_ip,
                           destination_ip, other_ioc, malware_url, referrer_url):

        login_page = Login(self.driver)
        homepage = login_page.login('admin', 'admin')
        all_incidents_page = homepage.click_security_incident_all_button()
        print("Before: " + all_incidents_page.get_total_rows())
        new_ticket_page = all_incidents_page.click_new_button()

        new_ticket_page.set_requested_by(requested_by)
        new_ticket_page.set_configuration_item(configuration_item)
        new_ticket_page.set_affected_user(affected_user)
        new_ticket_page.set_location(location)
        new_ticket_page.set_category(category)
        new_ticket_page.set_subcategory(subcategory)
        new_ticket_page.set_state(state)
        new_ticket_page.set_substate(substate)
        new_ticket_page.set_source(source)
        # new_ticket_page.set_business_critical(business_critical)
        # new_ticket_page.set_priority(priority)
        new_ticket_page.set_assignment_group(assignment_group)
        new_ticket_page.set_assign_to(assigned_to)
        new_ticket_page.set_short_description(short_description)
        new_ticket_page.set_description(description)
        new_ticket_page.set_destination_ip(destination_ip)
        new_ticket_page.set_other_ioc(other_ioc)
        new_ticket_page.set_additional_comment(additional_comment)
        new_ticket_page.set_work_notes(work_notes)
        new_ticket_page.set_secure_notes(secure_notes)
        new_ticket_page.set_source_ip(source_ip)
        new_ticket_page.set_malware_url(malware_url)
        new_ticket_page.set_referrer_url(referrer_url)

        new_ticket_page.click_submit_button()
        print("After: " + all_incidents_page.get_total_rows())



if __name__ == '__main__':
    unittest.main(verbosity=2)
