from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://www.peek.com"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message="Can't find element by locator {}".format(locator))

    def element_present(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message="Can't find element by locator {}".format(locator))
            return True
        except:
            return False

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message="Can't find elements by locator {}".format(locator))

    def find_elements_by_xpath(self, locator):
        return self.driver.find_elements_by_xpath(locator)

    def find_element_by_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def find_elements_count(self, locator):
        number_of_elements = len(self.find_elements(locator))
        print("NUMBER OF ELEMENTS ", number_of_elements)
        return number_of_elements

    def switch_to_iframe(self, locator, time=10):
        iframe = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                         message="Can't find element by locator {}".format(locator))
        self.driver.switch_to.frame(iframe)

    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                         message="Can't find element by locator {}".format(locator))
        element.click()

    def send_keys(self, locator, string, time=10):
        element =WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message="Can't find element by locator {}".format(locator))
        element.send_keys(string)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'