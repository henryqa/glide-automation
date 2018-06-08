import unittest
from basetestcase import BaseTestCase
from pages.home import HomePage
from pages.login import Login

class HomepageTest(BaseTestCase):

    def test_click_the_setting_button(self):
        login_page = Login(self.driver)
        homepage = login_page.login('admin', 'admin')
        all_incidents_page = homepage.click_security_incident_all_button()
        rows = all_incidents_page.get_total_rows()
        print("rows: " + rows)


if __name__ == '__main__':
    unittest.main(verbosity=2)