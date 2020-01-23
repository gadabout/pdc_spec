from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
import time
import random
from random import randrange
import re


class ElementLocators:
    LOCATION_SEARCH_FIELD = (By.ID, "homepage_location_search")
    SEARCH_BUTTON = (By.NAME, "Location Search Submit")
    BANNER_HEADER_CITY = "//strong[contains(text(),'{}')]"
    NAVIGATION_CITY = "//span[@data-reactid='61'][contains(.,'{}')]"
    ALL_ACTIVITIES = (By.XPATH, "//div[@class='padding-md-right padding-lg-bottom containers-Search-styles---mobileSearchResultsColumn']")
    CITY_IN_ACTIVITY = "//div[contains(.,'{}')]"
    TRENDING_ACTIVITIES_ON_MAIN_PAGE = "//div[@class='card rounded activity-tile-card']"
    AVAILABLE_DATES_IN_CALENDAR = "//li[@class='available regular']"
    AVAILABLE_DATES_IN_WIDGET = (By.XPATH, "//div[contains(@class, 'has-availability')]")
    BOOK_NOW_MAIN = (By.XPATH, "//h3[@class='calendar-book-now-button-link text-uppercase mb-0 semi-bold']")
    AVAILABLE_TIME_IN_WIDGET = (By.XPATH, "//a[contains(@class, 'not-sold-out')]")
    ERROR_TEXT_IN_WIDGET = "//div[contains(text(),'Please select a date and time before continuing')]"
    NUMBER_OF_TICKETS = (By.ID, "ember17604")
    ACTIVITY_HEADER = "//h1[@class='d-inline-flex mb-1 extra-bold']"
    WIDGET_IFRAME = "//iframe[@id='peek-embedded-frame']"
    TICKETS_INPUT = "((//div[@class='form-body'][contains(.,'Select Tickets')])[2]//input[@type='text'])[1]"
    SOLD_OUT = "//h3[contains(text(),'Sold out')]"
    TIME_IN_DROPDOWN = (By.XPATH, "//span[@class='time-text']")
    DROP_DOWN_OPTIONS = (By.XPATH, "//span[@class='ember-power-select-placeholder']")



class PeekPage(BasePage):

    def verify_page_has_loaded(self):
        assert self.page_has_loaded(), "THE REPORT HASN'T LOADED"

    def verify_header_city(self, city):
        return self.find_element_by_xpath(ElementLocators.BANNER_HEADER_CITY.format(city))

    def verify_navigation_city(self, city):
        return self.find_element_by_xpath(ElementLocators.NAVIGATION_CITY.format(city))

    def search_for_city(self, city):
        self.send_keys(locator=ElementLocators.LOCATION_SEARCH_FIELD, string=city)
        self.click_element(locator=ElementLocators.SEARCH_BUTTON)

    def enter_number_of_tickets(self, number):
        self.send_keys(locator=(By.XPATH, ElementLocators.TICKETS_INPUT), string=number)

    def get_activity_name(self):
        activity_name = self.find_element(locator=(By.XPATH, ElementLocators.ACTIVITY_HEADER)).text
        return activity_name

    def verify_city_in_activity(self, city):
        city_locator = ElementLocators.CITY_IN_ACTIVITY.format(city)
        return self.find_elements_count(locator=(By.XPATH, city_locator)) > 0

    def click_random_element(self, locator):
        number_of_elements = self.find_elements_count(locator)
        print('NUMBER OF ELEMENTS FOR {} IS '.format(locator), number_of_elements)
        random_element_num = str(randrange(1, number_of_elements))
        print('RANDOM  ELEMENTS NUMBER {} IS '.format(locator), random_element_num)
        random_element = locator + '[' + random_element_num + ']'
        print('RANDOM OF ELEMENT FOR {} IS '.format(locator), random_element)
        self.click_element(locator=(By.XPATH, random_element))

    # "Trending" activities on main page
    # "Some city" - activities on the page after a search for a specific city
    def select_random_activity(self):
        # self.click_random_element(ElementLocators.ALL_ACTIVITIES)
        activities = self.find_elements(ElementLocators.ALL_ACTIVITIES)
        random.choice(activities).click()

    def verify_correct_city_in_banner_header(self, city):
        self.go_to_site()
        self.search_for_city(city)
        city_header = self.verify_header_city(city)
        assert city_header, "THE HEADER CITY DOESN'T MATCH SEARCHED CITY {}.".format(city)

    def verify_correct_city_in_navigation(self, city):
        self.go_to_site()
        self.search_for_city(city)
        navigation_city = self.verify_navigation_city(city)
        assert navigation_city, "THE NAVIGATION CITY DOESN'T MATCH SEARCHED CITY {}.".format(city)

    def verify_correct_city_in_activity(self, city):
        self.search_for_random_activity(city)
        city_in_activity = self.verify_city_in_activity(city)
        assert city_in_activity, "THE CITY IN ACTIVITY DESCRIPTION DOESN'T MATCH SEARCHED CITY {}.".format(city)

    def verify_activitys_calendar(self, city):
        self.search_for_random_activity(city)
        dates_available = ElementLocators.AVAILABLE_DATES_IN_CALENDAR
        number_of_activities = self.find_elements_count(locator=(By.XPATH, dates_available))
        assert number_of_activities > 0, "NO AVAILABLE DAYS FOUND IN ACTIVITY."

    def increasing_number_of_tickets_beyond_availability(self, city):
        while True:
            self.search_for_random_activity(city)
            #If Sold Out find another activity
            if self.element_present(ElementLocators.BOOK_NOW_MAIN):
                pass
            else:
                continue
            time.sleep(0.5) #The Book Now button is not reliably working without time.sleep even with implicit wait
            self.click_element(locator=ElementLocators.BOOK_NOW_MAIN)
            print("CLICKED BOOK NOW")
            self.switch_to_iframe(locator=(By.XPATH, ElementLocators.WIDGET_IFRAME))
            dates = self.find_elements(ElementLocators.AVAILABLE_DATES_IN_WIDGET)
            random.choice(dates).click()
            if not self.element_present(ElementLocators.AVAILABLE_TIME_IN_WIDGET):
                self.click_element(locator=ElementLocators.DROP_DOWN_OPTIONS)
                time_in_dropdown = self.find_elements(ElementLocators.TIME_IN_DROPDOWN)
                random.choice(time_in_dropdown).click()
            else:
                times = self.find_elements(ElementLocators.AVAILABLE_TIME_IN_WIDGET)
                random.choice(times).click()
            self.enter_number_of_tickets("100")
            error_message = self.find_elements((By.XPATH, ElementLocators.ERROR_TEXT_IN_WIDGET))
            self.driver.switch_to.default_content()
            break
        assert len(error_message) > 0, "NO ERROR MESSAGE SHOWN AFTER SELECTING TOO MANY TICKETS"

    def search_for_random_activity(self, city):
        self.go_to_site()
        self.search_for_city(city)
        self.select_random_activity()
