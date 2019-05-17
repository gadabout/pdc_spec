require "selenium-webdriver"
require "rspec"

def main_search(location)
    @driver.find_element(:class, 'geosuggest__input').send_keys(location)
    @driver.find_element(:class, 'components-Forms-Search-style---homeDatePicker').click
    @driver.find_element(:class, 'components-Forms-Search-style---homeButton').click
    sleep 5
end
