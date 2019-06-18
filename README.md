# Peek.com Specs

A repository for creating test automation for www.peek.com

![](peek-squarelogo.png)

## How to use this repo

Fork this repo and go through the [user stories](Specs.md) and create automated tests for the provided acceptance criteria. Include as many test cases as you like. Any pattern/framework will be accepted, but please limit your technologies to JS, Ruby, or Python. Commit your tests and support code and open a pull request in the original repo for your fork.

The code in this repo should be easily executable. Please provide instructions on dependencies, configuration, and the development process in the Notes section below.

Good luck!

## Notes

This repository contains code to leverage Selenium Webdriver (JS) to test aspects of the Peek.com website.  Tests are implemented for each requirement based on my intepretation of said requirement:
* Search filters correctly apply after initial search
  * *Perform search at peek.com, then click on a search filter at the resulting page and verify the number of results*
* Categories appear based on location inventory
  * *Perform search at peek.com, then verify the category and quantity values for the elements at the top of the screen*
* When completed, the quiz should provide a search form - when I search I should see my classification listed at the top of my results
  * *Answer all nine personality questions to retrieve the classification name, then verify the search form element, then perform a (blank) search and verify the classification name at the resulting page matches (e.g. 'An Insider', 'An Adventurer', etc.)*
* The activity's calendar widget populates with bookable days
  * *Open a booking page and verify the calendar element*
* Increasing the number of selected tickets beyond the availability prevents me from booking that timeslot
  * *Open a booking page, click on the + button for a specified number of times to go over the maximum bookable amount, then verify that the Book Now button is disabled*
* The "Book Now" Button opens a widget flow with my timeslot and ticket(s) selected at checkout
  * *Open a booking page, record month, date, and time selected in the calendar widget, then click on Book Now and verify against the resulting widget*


Please download test.js, data.js, and package.json from this repository.  In addition, install the following:
- Node.js (v10.15.0)
- npm (6.4.1)
- selenium-webdriver (4.0.0-alpha.1)  (installed locally, via 'npm install selenium-webdriver')
- Mocha (6.1.4)  (installed locally, via 'npm install --save-dev mocha')
- chromedriver (if running Chrome) for the OS of the target computer
- geckodriver (if running Firefox) for the OS of the target computer

Place in the same directory, then run by typing 'npm test'.


data.js contains some configurable values related to testing.  For instance, change the "browser" value to change the browser to use for testing; change the "spec1.input.searchTerm" value to change the search term to use at the beginning of the tests for the first spec.


