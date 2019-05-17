require_relative 'peek_helper'

#Feature: As a consumer visiting Peek.com I would like to be able to book an activity
#The activity's calendar widget populates with bookable days
#Increasing the number of selected tickets beyond the availability prevents me from booking that timeslot
#The "Book Now" Button opens a widget flow with my timeslot and ticket(s) selected at checkout

describe "Book a new activity" do
  before(:all) do
    @driver = Selenium::WebDriver.for :chrome
    @base_url = "http://peek.com"
    @driver.manage.window.maximize
    @driver.get(@base_url)
  end
  it "searches for new activity" do
    location="Santa Cruz, Ca, USA"
    activity="Surfing"
    main_search(location)
    searchlocation = @driver.find_element(:xpath, "//input[@value='#{location}']")
    @driver.action.move_to(searchlocation).perform
    expect(searchlocation.attribute("value")).to eql(location)
    @driver.find_element(:class, "keyword").send_keys("Surfing")
    @driver.find_element(:class, "btn-primary").click
    sleep 2
    total_search_results = @driver.find_element(:class, "containers-Search-styles---resultsCount").text
    expect(total_search_results).to include "Surfing"
  end
  it "selects first vendor" do
    @driver.find_element(:class, "components-ActivityRow-style---panel").click
    sleep 2
    @driver.find_element(:class, "containers-Activities-HeroPhotoWidget-style---bookingButton").click
    booking_cal = @driver.find_element(:class, "components-BookingWidget-style---main")
    @driver.action.move_to(booking_cal).perform
    available_dates = @driver.find_elements(:class, "available")
    puts available_dates
  end
end
