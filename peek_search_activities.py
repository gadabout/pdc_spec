"""
Written by Michael McGreevy 071319

This script tests the following user story:
Feature: As a consumer visiting Peek.com I would like to be able to search for activities near me
	* Categories appear based on location inventory
	* Search filters correctly apply after initial search


For the first item, two criteria must be passed: the web page rendered after the initia search is performed 
must contain the original search criteria (e.g., "Costa Rica") and the number of associated activities mentioned in two locations
(e.g., "13 Things to do in/Costa Rica" and "All Activities 13/Adventures") on the rendered page must equal other.

For the second item, a price range filter is applied after the location region has been searched for.  A check is then performed 
that only activities whose price falls in the range are displayed.

There are a couple of weaknesses that should be noted with these tests:
1) The tests for the first item, above, assumes the returned activities are correct if the text of (for example) 
	"13 things to do in/Costa Rica" and "All Activities/13 Adventures"(if Costa Rica was the original search criteria) is displayed.
	What if the text is displayed but the rendered web page is displaying activities for a different region?
2) When testing the price range filter, the script assumes there are < 21 activities associted with the original search criteria.
If there are more activities (e.g., as there are with San Francisco), the test will fail, since multiple pages will be returned.  
	The script currently only works with one page of activities.

To help counteract these weaknesses, the script runs through 4 different sets of data.  With the exception of San Francisco, these 
data were all picked to have fewer than 21 associated activities.  SF will intentionally fail, to verify a graceful recovery and
to verify failure notification.


Note all results are logged to a text file called "search_activites.txt", located in the same directory as the script.

TODO for improvements:
* Add an outer nested loop to use all common web browsers/drivers
* Add checks for all price ranges
* Support geo regions with more than 20 activities (multiple pages)
* Add additional try/except error checking
* Possibly split test out into indie functions to improve readibility and portability

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import sys

passed = True												# global pass fail.  Stays True only if all tests pass
region_names = ["Costa Rica", "Bahamas", "San Francisco, CA, USA", "Belize"]			# the 4 test loctions/region names (SF will fail)
#region_names = ["San Francisco, CA, USA"]			# the three test loctions/region names
star_line_80 = "\n" + "*" * 80 + "\n" + "*" * 80 + "\n"		# a text line designed to help demark locations in the results log
star_line_40 = "\n" + "*" * 40 + "\n"						# a text line designed to help demark indie tests in the results log

try:				# Can the file be opened?
	f = open("search_activities.txt", "a+")					# open the test log with handle 'f'
except IOError:			# No!  The file could not be opened.
	print("Couldn't open search_activities.txt", f)
	sys.exit()			# Die.

f.write("\n\n\n\nThis test run was executed on {}.\n".format(time.ctime(time.time())))		# log the time
for region_name in region_names:							# this loop performs an iter for each region name
	driver = webdriver.Firefox()							# set up the browser driver
	driver.implicitly_wait(5)								# wait up to 5 seconds for web page elements to be drawn
	driver.get("http://www.peek.com")						# open the root web page

	f.write(star_line_80)
	f.write("Tests for region name = {}.".format(region_name))			# note region name in the log
	f.write(star_line_80)

	######################################################################################
	# Beginning of test to verify the entered geographical area returns the correct related activities
	######################################################################################
	f.write(star_line_40)
	f.write("Test for initial region search.")				# note the test in the log
	f.write(star_line_40)

	gs_input = driver.find_element_by_class_name("geosuggest__input")		# locate the inital search box element
	gs_input.clear()
	gs_input.send_keys(region_name)							# type in the region name to search
	gs_input.send_keys(Keys.RETURN)							# hit the return key a few times
	time.sleep(2)
	gs_input.send_keys(Keys.RETURN)
	time.sleep(2)
	gs_input.send_keys(Keys.RETURN)

	# location.text is the region name displayed at the top of the page after the initial search.  
	# Should match the initial search criteria (first check to pass the test mentioned in the general comments above)
	location = driver.find_element_by_class_name("containers-Search-styles---regionName")	# verify the resulting text matches
	if location.text == region_name:
		f.write("The rendered page region name is the same as the original search criteria.\nInitial region search test passed.\n\n")	# log test pass/fail
	else:
		"The rendered page region name is NOT the same as the original search criteria.\nInitial region search FAILED!\n\n"
		passed = False 			# set global passed/fail to False

	# x_things_to_do_in should contain the text at the top of the page resulting from the initial search that says something like
	# "13 Things to do in"
	try:
		x_things_to_do_in = driver.find_element_by_xpath('//div[@class="containers-Search-styles---noActivityBannerCount containers-Search-styles---resultsCount padding-none"]')
	except:
		f.write("Coulnd't get the x_things_to_do_in web element for {}.  Perhaps this region name has more than 20 activities?\nContinuing with the next region\n\n".format(region_name))
		passed = False
		continue
	match = re.search('(\d+)', x_things_to_do_in.text)					# get the integer text in x_things_to_do_in
	activity_count = match.group(1)									# activity_count now has this integer
	
	# all_activites_x_adventure will contain the bottom text associated with the user's initial search -- e.g., "All Activities/13 Adventures"
	all_activites_x_adventure = driver.find_element_by_class_name("containers-Search-styles---categoriesResultsCount")	
	match = re.search('(\d+)', all_activites_x_adventure.text)			# get the integer text in all_activites_x_adventure
	number_of_acts = match.group(1)									# number_of_acts now has this integer
	if activity_count == number_of_acts:							# do the two text integers equal each other? (second pass criteria)
		f.write("The number of activities ({}) found on both locations of the web page equal each other.\nActivity count test passed.\n".format(number_of_acts))
	else:
		f.write("The number of activities found on both locations of the web page do NOT equal each other.\nActivity count test FAILED!\n")
		passed = False
	

	######################################################################################
	# Beginning of test to verify the price range filter 
	######################################################################################
	f.write(star_line_40)
	f.write("Test for price range filtering.")			
	f.write(star_line_40)
	# unfiltered_activites is a list of activity descriptions before the price range filter is applied
	unfiltered_activites = driver.find_elements_by_xpath('//div[@class="components-ActivityRow-style---activityRowLink"]')

	# find the price filter UI element:
	price_filter = driver.find_element_by_xpath('//div[@class="containers-Search-styles---priceRangesHeader margin-none-top"]').click()
	time.sleep(2)
	price_range = driver.find_element_by_name("$50 - $100").click()		# select the $50 to $100 price range
	time.sleep(2)

	# filtered_activities will contain a list of all of the remaining/filtered activities
	filtered_activities = driver.find_elements_by_xpath('//div[@class="components-ActivityRow-style---activityRowLink"]')
	filtered_activities_count = len(filtered_activities)


	if int(activity_count) == filtered_activities_count:		# this conditional verifies the price range filter actuall omitted an activity
		f.write("No activity has a price out of the $50 to $100 price range.\nTest is INVALID!  Find a different geo region to work with.\n")	
		passed = False
	else:
		f.write("At least one activity has a prices out of the $50 to $100 price range.\nTest is valid.\n\n")	

	f.write("The number of filtered activities listed is {}.".format(filtered_activities_count))
	# this loops goes through the filtered activities and verifies their price falls into the correct range
	for i in range(filtered_activities_count):		
		filtered_cost_flag = True			# sadness, if ever false
		filtered_cost = re.findall('\d+', filtered_activities[i].text)
		if int(filtered_cost[0]) < 50 or int(filtered_cost[0]) > 100:
			f.write("  There are activities outside of the filtered price range.\nFiltered price range test FAILED!\n")
			filtered_cost_flag = False
			passed = False
	if filtered_cost_flag == True:
		f.write("  All filtered costs are within the filtered price range.\nFiltered price test passed.\n")

	driver.close()								# close the web browser for this region iteration
	f.write("\n\n\n")
if passed == True:
	f.write("ALL TESTS FOR ALL REGIONS PASSED.")
else:
	f.write("AT LEAST ONE TEST FAILED!")
f.write("\n\n\n")

f.close()			# Close the log file.
