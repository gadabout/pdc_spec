require "selenium-webdriver"
require "rspec"

# Feature: As a consumer visiting Peek.com I would like to be able to search for activities near me
#  - Search filters correctly apply after initial search
#  - Categories appear based on location inventory
describe "Peek.com landing page funtionality" do
  before(:all) do
    @driver = Selenium::WebDriver.for :chrome
    @base_url = "http://peek.com"
    @driver.manage.window.maximize
    #@driver.manage.timeouts.implicit_wait * 60
    #
    SEARCHLOCATION="San Francisco Peninsula"
  end

  it "should be on the landing page" do
    @driver.get(@base_url)
    landingPageText = @driver.find_element(:class, 'containers-Home-Hero-style---title').text
    expect(landingPageText).to eql('What do you want to do today?')
  end

  it "should search for San Francisco Peninsula as destination city" do
    @driver.find_element(:class, 'geosuggest__input').send_keys(SEARCHLOCATION)
    @driver.find_element(:class, 'components-Forms-Search-style---homeDatePicker').click
    @driver.find_element(:class, 'components-Forms-Search-style---homeButton').click
    sleep 5
    locationResult=@driver.find_element(:css, '.containers-Search-styles---regionName > span > strong').text
    expect(locationResult).to eql(SEARCHLOCATION)
  end

  it "default search location on results page should be set to San Francisco Peninsula" do
    searchlocation = @driver.find_element(:xpath, "//input[@value='San Francisco Peninsula']").attribute("value")
    expect(searchlocation).to eql(SEARCHLOCATION)
  end

  it "should cover proximity of a 25 miles in the initial results" do
    activitiesresults = @driver.find_elements(:class, 'components-ActivityRow-style---distance')
    for activity in  activitiesresults 
      distance  = activity.text
      dissplit = distance.split(" ")
      expect(dissplit[0].to_i).to be < 25.0
    end
  end

end
