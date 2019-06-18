# Peek.com Specs

A repository for creating test automation for www.peek.com

![](peek-squarelogo.png)

## How to use this repo

Fork this repo and go through the [user stories](Specs.md) and create automated tests for the provided acceptance criteria. Include as many test cases as you like. Any pattern/framework will be accepted, but please limit your technologies to JS, Ruby, or Python. Commit your tests and support code and open a pull request in the original repo for your fork.

The code in this repo should be easily executable. Please provide instructions on dependencies, configuration, and the development process in the Notes section below.

Good luck!

## Notes

This repository contains code to leverage Selenium Webdriver (JS) to test aspects of the Peek.com website.

Please download test.js, data.js, and package.json from this repository.  In addition, install the following:
Node.js (v10.15.0)
npm (6.4.1)
selenium-webdriver (4.0.0-alpha.1)  (installed locally, via 'npm install selenium-webdriver')
Mocha (6.1.4)  (installed locally, via 'npm install --save-dev mocha')
chromedriver (if running Chrome) for the OS of the target computer
geckodriver (if running Firefox) for the OS of the target computer

To run, type 'npm test'.




