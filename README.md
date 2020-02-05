# Peek.com Specs

A repository for creating test automation for www.peek.com

![](peek-squarelogo.png)

## How to use this repo

Fork this repo and go through the [user stories](Specs.md) and create automated tests for the provided acceptance criteria. Include as many test cases as you like. Any pattern/framework will be accepted, but please limit your programming languages to JS, Ruby, or Python. Commit your tests and support code and open a pull request in the original repo for your fork.

The code in this repo should be easily executable. Please provide instructions on dependencies, configuration, and the development process in the Notes section below.

Good luck!

## Notes

Notes go here.

To peek reviewer,

To run tests, go to terminal `$ npm test`. This will execute tests within the specs directory. Ensure you have dependencies installed prior `$ npm install`.

Dependencies can be found in package.json file. The dependencies I chose for this project are:
babel - allows contributors to code in the lastest EMCAScript
webdriverio - an implementation of Selenium
mocha - provides test structure
chai - assertion library
allure - test reporting

This framework follows the Page Object Model design pattern where a page object is an object-oriented class that serves as an interface to a page of a web application being tested. To make configurations to this framework, open wdio.conf.js file. There are notes within this file.

Once tests finish execution, you can see see logs and reports located in output directory.

Please don't hestitate to ask me any questions!