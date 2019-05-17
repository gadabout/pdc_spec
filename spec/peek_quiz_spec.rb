require "selenium-webdriver"
require "rspec"

# Feature: As a consumer visiting Peek.com I would like to take a personality quiz to cater search results to my preferences
# When completed, the quiz should provide a search form - when I search I should see my classification listed at the top of my search results

describe "Take personality quiz test, verify search results catered to my preferences." do
  before(:all) do
    @driver = Selenium::WebDriver.for :chrome
    @base_url = "http://peek.com"
    @driver.manage.window.maximize
    #@driver.manage.timeouts.implicit_wait * 60
  end

  it "should locate personality quiz on the landing page" do
    @driver.get(@base_url)
    landingPageText = @driver.find_element(:class, 'components-Modals-PersonalityQuiz-style---quizDescription').text
    expect(landingPageText).to eql('Help us handpick experiences just for you')
  end

  it "should be able to click on quiz selections" do
    leftSelection = @driver.find_element(:class, 'components-PersonalityQuiz-QuizImagePicker-style---imageContainer')
    rightSelection = @driver.find_element(:class, 'components-PersonalityQuiz-QuizImagePicker-style---imageContainer')
    currentStep = 'components-PersonalityQuiz-PhotoQuizFlow-style---currentStep'
    totalSteps = 'components-PersonalityQuiz-PhotoQuizFlow-style---totalSteps'
    quizResult = 'components-Modals-PersonalityQuiz-style---personalityResultName'
    quizResultText = 'A Foodie'
    quizselections = [ "right", "left", "left", "right", "left", "left", "left", "right", "left"]
    @driver.action.move_to(leftSelection).perform
    #take a quiz
    quizselections.each_with_index do |val, index|
      case val
      when "left"
        leftSelection.click
      when "right"
        rightSelection.click
      end
    end
    #verify quiz results
    sleep 1
    locationResult=@driver.find_element(:class, quizResult).text
    expect(locationResult).to eql(quizResultText)
  end

  it "should be able to search by destination after takling perfonality quiz" do
    search_input = @driver.find_element(:css, '.search-page-form > .form-group .geosuggest__input')
    search_button = @driver.find_element(:css, '.components-Forms-Search-style---quizButton')
    focus_area = @driver.find_element(:class, 'containers-Home-style---title')
    @driver.action.move_to(focus_area).perform
    search_input.send_keys("Dallas, TX, USA")
    search_button.click
  end
end
