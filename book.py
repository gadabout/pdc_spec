
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PeekSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.peek.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_peek_search(self):
        driver = self.driver
        driver.get("https://www.peek.com/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Great activities wherever you live, wherever you go'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Great activities wherever you live, wherever you go'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Great activities wherever you live, wherever you go'])[1]/following::input[1]").send_keys("san francisco, Ca")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Great activities wherever you live, wherever you go'])[1]/following::li[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='California 1, San Francisco, CA, USA'])[1]/following::button[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='All Activities'])[2]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(82)'])[2]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(55)'])[2]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(42)'])[2]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(28)'])[3]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(28)'])[4]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(20)'])[3]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(20)'])[4]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(16)'])[2]/following::div[3]").click()
        driver.find_element_by_name("Over $250").click()
        driver.find_element_by_name("$100 - $250").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Under $50'])[1]/following::label[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Price'])[1]/following::label[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
