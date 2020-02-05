from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from values.strings import search_value
from selenium.webdriver.common.keys import Keys


class HomeScreen():

    def __init__(self, driver):
        self.driver = driver

        self.homepage_search = self.driver.instance.find_element_by_id("homepage_location_search")
        self.search_button = self.driver.instance.find_element_by_class_name("homepage-search-button")
        self.personality_quiz_img = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//div[@class='personality-quiz-border']/div/div[1]/img")))

        self.activity_image = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                By.XPATH,"//div[@class='card rounded activity-tile-card']")))

    def setLocationValue(self): 
        self.homepage_search.send_keys(search_value)
        
    def click_search_button(self):
        self.search_button.click()
    
    def personality_quiz_image(self):
        self.personality_quiz_img.click()

    def get_personality_results(self):
        self.personality_result = WebDriverWait(self.driver.instance, 300).until(
            EC.visibility_of_element_located((
                By.XPATH,"//span[@class='personality-result-name']")))
        return self.personality_result.text
    
    def search_with_quiz_results(self):
        self.search_location_quiz = WebDriverWait(self.driver.instance, 1000).until(
            EC.element_to_be_clickable((
                By.XPATH, "//div[@class='search-form']")))
        personality_result_text = self.get_personality_results()

        search_input = self.driver.instance.find_element_by_xpath("//form[@id='personality_quiz_location_form']/div/div/div/div/input")
        search_input.send_keys(personality_result_text)
        search_input.send_keys(Keys.ENTER)

    def check_activity_calendar(self):
        self.activity_image.click()

        
    def validate_attractions(self):
        atraction_image = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                By.XPATH,"//li[@class='glide__slide']")))
        atraction_image.click()






