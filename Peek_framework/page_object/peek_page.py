from selenium.webdriver.common.by import By
from page_object.base_page import BasePage

class ElementLocators:

    LOCATION_SEARCH_FIELD = (By.ID, "homepage_location_search")
    SEARCH_BUTTON = (By.NAME, "Location Search Submit")
    BANNER_HEADER = "//h1[@class='banner-header'][contains(.,'{}')]"


class PeekPage(BasePage):

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def verify_page_has_loaded(self):
        assert self.page_has_loaded(), "THE REPORT HASN'T LOADED"

    def search_for_city(self, city):
        self.send_keys(locator=ElementLocators.LOCATION_SEARCH_FIELD, string=city)
        self.click_element(locator=ElementLocators.SEARCH_BUTTON)
        city_header = self.find_element(By.NAME, ElementLocators.BANNER_HEADER.format(city))
        assert city_header

