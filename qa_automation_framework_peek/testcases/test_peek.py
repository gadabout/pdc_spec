
import unittest

from pageobjects.searchpage import SearchPage
from pageobjects.homescreen import HomeScreen
from pageobjects.activitypage import ActivityPage
from values import strings
from webdriver import Driver
from values.strings import search_value


class TestPeek(unittest.TestCase):
    
    def setUp(self):

        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    #Validates first use case. Verify that search filters correctly applies and category applies based on value from strings.py
    def test_validate_pages_data(self):

        home_screen = HomeScreen(self.driver)

        home_screen.setLocationValue()
        home_screen.click_search_button()

        search_page = SearchPage(self.driver)

        initial_search_location= search_page.search_result_location()

        assert search_value == initial_search_location

    #Validates second use case. Verify that personality quiz works correctly and search, based on quiz results, return correct categories.
    def test_validate_quiz(self):
        home_screen = HomeScreen(self.driver)

        self.driver.instance.implicitly_wait(30)

        for image in range(0,9):
            home_screen.personality_quiz_image()

        results = home_screen.get_personality_results()

        home_screen.search_with_quiz_results() 

        search_page = SearchPage(self.driver)
        personality_quiz_search = search_page.input_values_in_seach_box(results)
        assert results in personality_quiz_search
    
    #Validates third use case. Verify calendar and booking works correctly.
    def test_validate_book_an_activity(self):
        home_screen = HomeScreen(self.driver)
        home_screen.check_activity_calendar()

        activity_page = ActivityPage(self.driver)
        activity_page.validate_available_day_for_booking()
        activity_page.validate_book_now_button()

    #Validates third use case. When user icrease the number of selected tickets beyond the availability, widget doesn't allow you to book an activity for that day.
    def test_validate_counting_tickets(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_attractions()

        activity_page = ActivityPage(self.driver)
        activity_page.validate_book_now_button()
        activity_page.validate_tickets()
        
    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    print ('Hello, world!')
    unittest.main()