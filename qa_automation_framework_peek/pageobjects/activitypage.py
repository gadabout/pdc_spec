from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time 
from datetime import date


class ActivityPage():

    def __init__(self, driver):
        self.driver = driver
        self.available_dates = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_all_elements_located((
                By.XPATH, "//div[@class='month-wrapper']/ul[2]/li/a")))
        self.book_now_button = self.driver.instance.find_element_by_xpath("//div[@id='book-now-spinnaker']/h3")


    def validate_available_day_for_booking(self):
        print(len(self.available_dates))
        assert len(self.available_dates)>0
    
    def validate_book_now_button(self):
        self.book_now_button.click()
        self.calendar_widget = WebDriverWait(self.driver.instance, 15).until(
            EC.visibility_of_element_located((
                By.XPATH,"//div[@id='peek-booking-flow-placeholder']")))
        assert self.calendar_widget.is_displayed()

    def validate_tickets(self):
        time.sleep(40)
        iframe = self.driver.instance.find_element_by_xpath("//iframe[@id='peek-embedded-frame']")
        self.driver.instance.switch_to.frame(iframe)

        date = self.driver.instance.find_elements_by_xpath("//div[@class='ember-view __ui-internal__calendar-day__1e941 calendar-day has-availability not-sold-out availability-style-price-range-2 clickable-days']")
        date[3].click()
        select_time = self.driver.instance.find_element_by_xpath("//a[@class='ember-view __ui-internal__time-option__e63ce time-option is-bookable not-sold-out show-as-button']")
        select_time.click()

        quantity_link = self.driver.instance.find_elements_by_xpath("//div[@class='ember-view pro-form-quantity']/span/a")
        time.sleep(10)
        
        for i in range(2):
            quantity_link[3].click()


        WebDriverWait(self.driver.instance, 25).until(
            EC.presence_of_element_located((
                By.XPATH,"//*[text()='Please select a date and time before continuing']")))





