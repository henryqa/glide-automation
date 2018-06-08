import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://34.220.37.208:1600/navpage.do')


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)