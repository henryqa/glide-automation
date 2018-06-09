import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome("../drivers/chromedriver")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://34.214.114.240:1600/navpage.do')


    def tearDown(self):
        self.driver.quit()