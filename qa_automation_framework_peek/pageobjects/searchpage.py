from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time 


class SearchPage():

    def __init__(self, driver):
        self.driver = driver
        self.search_locator=self.driver.instance.find_element_by_css_selector(".containers-Search-styles---regionName>span>strong")
        self.search_text_box = self.driver.instance.find_element_by_xpath("//div[@class='containers-Search-styles---searchPageSticky hidden-sm hidden-xs hidden-md']/div/div/div/div/form/div/div/div/input")

    def search_result_location(self):
        return self.search_locator.text

    def input_values_in_seach_box(self,value):
        self.search_text_box.send_keys(value)
        self.search_text_box.send_keys(Keys.ENTER)

        time.sleep(5)
        preference_search_results = WebDriverWait(self.driver.instance, 30).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "containers-Search-styles---noActivityBannerCount")))

        return preference_search_results.text


