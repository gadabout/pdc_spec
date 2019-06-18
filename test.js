var webdriver = require('selenium-webdriver');
var assert = require('assert');
var data = require('./data.js');


describe('Tests for https://www.peek.com', function() {

	// Declarations, initializations.
	var browser;
	var waitTimeout = 10000;
	this.timeout(60000);  // Override mocha.js timeout
	
	
	// Setup and Teardown for entire suite
	before(async function() {
		browser = await new webdriver.Builder().usingServer().withCapabilities({'browserName': data.browser }).build();
	});


	after(function() {
		return browser.quit();
	});


//*
	// Spec 1
	describe('As a consumer visiting Peek.com I would like to be able to search for activities near me', function() {	

		// Setup and Teardown
		beforeEach(async function() {
			await browser.get('https://www.peek.com')
			
			await browser.findElement(webdriver.By.className('geosuggest__input')).sendKeys(data.spec1.input.searchTerm)
			
			// Click on the autosuggest to ensure that the search term is correctly registered. 
			var element = await browser.wait(webdriver.until.elementLocated(webdriver.By.className('geosuggest-item--active')), waitTimeout)
			await browser.wait(webdriver.until.elementIsVisible(element), waitTimeout).click()

			await browser.findElement(webdriver.By.className('components-Forms-Search-style---homeButton')).click()
		});


		// Test Cases
		it('should apply search filters correctly after initial search', async function() {
			// Record the original element and its results.
			var element = await browser.wait(webdriver.until.elementLocated(webdriver.By.className('containers-Search-styles---resultsCount')), waitTimeout);
//			var results1 = parseInt(await element.getText())
			
			// Set the filters.
			for (var i = 0; i < data.spec1.input.filter.length; i++) {
				await browser.findElement(webdriver.By.css('input[name="' + data.spec1.input.filter[i] +'"]')).click()				
			}
			
			// Wait for results count to go stale, then get the new results.
			await browser.wait(webdriver.until.stalenessOf(element))
			var results2 = parseInt(await browser.wait(webdriver.until.elementLocated(webdriver.By.className('containers-Search-styles---resultsCount')), waitTimeout).getText())
			
			// Evaluate filtered results.
//			assert(results1 > results2);
			assert.equal(data.spec1.output.results, results2);
		});


		it('should show categories based on location inventory', async function() {
			// Build the results list.
			var catElement = await browser.wait(webdriver.until.elementsLocated(webdriver.By.css('.containers-Search-ParentCategoryFacetTiles-style---tileColumn [data-metrics-category-name]')), waitTimeout)
			var cat = [];
			for (var i = 0; i < catElement.length; i++) {
				cat.push({ name: await catElement[i].getAttribute('data-metrics-category-name'), quantity: await catElement[i].getAttribute('data-metrics-category-quantity')})
			}
			
			// Verify.
			for (var i = 0; i < data.spec1.output.cat.length; i++) {
				assert.equal(data.spec1.output.cat[i].name, cat[i].name, 'Category name mismatch at index ' + i)
//				assert.equal(data.spec1.output.cat[i].quantity, cat[i].quantity, 'Category quantity mismatch at index ' + i)
			}
		});

	});
//	*/


//*
	// Spec 2
	describe('As a consumer visiting Peek.com I would like to take a personality quiz to cater search results to my preferences', function() {

		// Setup and Teardown
		before(async function() {
			await browser.get('https://www.peek.com')

			for (var i = 0; i < data.spec2.input.q.length; i++) {
				if (!data.spec2.input.q[i]) {
					await browser.wait(webdriver.until.elementIsVisible(browser.findElement(webdriver.By.css('.components-PersonalityQuiz-QuizImagePicker-style---imageContainer.margin-md-right')))).click()
				}
				else {
					await browser.wait(webdriver.until.elementIsVisible(browser.findElement(webdriver.By.css('.components-PersonalityQuiz-QuizImagePicker-style---imageContainer.margin-xs-top')))).click()					
				}
			}
			
			await browser.wait(webdriver.until.elementLocated(webdriver.By.className('components-Modals-PersonalityQuiz-style---resultsModal')), waitTimeout);
		});


		// Test Cases
		it('should provide a search form when the quiz is completed', async function() {
			await browser.findElement(webdriver.By.className('components-Modals-PersonalityQuiz-style---searchFields'))
		});

		it('should show my classification listed at the top of my search results when I search', async function() {
			var result1 = await browser.findElement(webdriver.By.className('components-Modals-PersonalityQuiz-style---personalityResultName')).getText()
			await browser.findElement(webdriver.By.className('components-Forms-Search-style---quizButton')).click()
			var result2 = await browser.wait(webdriver.until.elementLocated(webdriver.By.className('components-PersonalityQuiz-PersonalityResult-style---personalityResultName')), waitTimeout).getText()

			assert.equal(result1, result2);
		});		
	});
//	*/


//*
	// Spec 3
	describe('As a consumer visiting Peek.com I would like to be able to book an activity', function() {

		// Setup and Teardown
		beforeEach(async function() {
			await browser.get(data.spec3.input.url)
		});

		
		// Test Cases
		it('should populate the activity\'s calendar with bookable days', async function() {
			await browser.findElement(webdriver.By.css('div[name="bookingWidget"]'))
		});


		it('should prevent me from booking the timeslot when increasing the number of selected tickets beyond the availability', async function() {
			// Click away the cookies banner because it blocks the +/- buttons.
			await browser.findElement(webdriver.By.className('components-GdprPrompt-style---closeButton')).click()
			
			for (var i = 0; i < data.spec3.input.ticketsMax; i++) {
				await browser.wait(webdriver.until.elementLocated(webdriver.By.xpath('//i[@class="fa fa-plus"]/..')), waitTimeout).click()			
			}			
//			await browser.wait(webdriver.until.elementLocated(webdriver.By.className('text-danger')), waitTimeout)
			await browser.wait(webdriver.until.elementLocated(webdriver.By.css('.padding-md button:disabled')), waitTimeout)			
		});


		it('should open a widget flow with my timeslot and ticket(s) selected at checkout when I press the "Book Now" button', async function() {
			// Get the calendar widget's month, date, time.
			var resultMonth1 = (await browser.findElement(webdriver.By.className('monthLabel')).getText()).slice(0, 3).toUpperCase()
			var resultDate1 = await browser.wait(webdriver.until.elementLocated(webdriver.By.css('.calendarDay.selected')), waitTimeout).getText()			

			var timeDropdown = await browser.wait(webdriver.until.elementLocated(webdriver.By.id('formControlsSelect')), waitTimeout)
			var resultTime1 = (await timeDropdown.findElement(webdriver.By.css('option[value="' + await timeDropdown.getAttribute('value') + '"]')).getText()).toUpperCase()

			// Click 'Book Now', then switch to the booking widget's iframe when it appears.
			await browser.findElement(webdriver.By.className('padding-md')).click()			
			await browser.wait(webdriver.until.ableToSwitchToFrame(webdriver.By.id('peek-embedded-frame')), waitTimeout)

			// Get the booking widget's month, date, time.
			var dateElement = (await browser.wait(webdriver.until.elementLocated(webdriver.By.css('div.date-col')), waitTimeout).getText()).split('\n')
			var resultMonth2 = dateElement[1]
			var resultDate2 = dateElement[0]

			var resultTime2 = (await browser.wait(webdriver.until.elementLocated(webdriver.By.css('div.time-col')), waitTimeout).getText()).split('\n').join('')
			
			// Verify the two months, dates, and times.
			assert.equal(resultMonth1, resultMonth2)
			assert.equal(resultDate1, resultDate2)
			assert.equal(resultTime1, resultTime2)
		});
	});
//	*/

});