from logging import Logger
import pytest


class TestReport:
    log = Logger('TestReport')

    # Verifying the main page loads after opening
    def test_verify_page_loads(self, report_page):
        self.log.info("Checking if {} page is loaded.".format(report_page.driver.current_url))
        report_page.verify_page_has_loaded()

    # Search filters correctly apply after initial search. Categories appear based on location inventory.
    @pytest.mark.parametrize('city', ["San Francisco", "New York", "Chicago"])
    def test_verify_correct_city_in_banner_header(self, report_page, city):
        report_page.verify_correct_city_in_banner_header(city)

    # Search filters correctly apply after initial search. Categories appear based on location inventory.
    @pytest.mark.parametrize('city', ["San Francisco", "New York", "Chicago"])
    def test_verify_correct_city_in_navigation(self, report_page, city):
        report_page.verify_correct_city_in_navigation(city)

    # Search filters correctly apply after initial search. Categories appear based on location inventory.
    @pytest.mark.parametrize('city', ["San Francisco", "New York", "Chicago"])
    def test_verify_correct_city_in_activity(self, report_page, city):
        report_page.verify_correct_city_in_activity(city)

    # The activity's calendar widget populates with bookable days
    @pytest.mark.parametrize('city', ["San Francisco"])
    def test_verify_activitys_calendar(self, report_page, city):
        report_page.verify_activitys_calendar(city)

    # Increasing the number of selected tickets beyond the availability prevents me from booking that timeslot
    @pytest.mark.parametrize('city', ["San Francisco"])
    def test_increasing_number_of_tickets_beyond_availability(self, report_page, city):
        report_page.increasing_number_of_tickets_beyond_availability(city)
