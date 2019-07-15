"""
Written by Michael McGreevy 071419

Feature: As a consumer visiting Peek.com I would like to be able to book an activity
* The activity's calendar widget populates with bookable days
* Increasing the number of selected tickets beyond the availability prevents me from booking that timeslot
* The "Book Now" Button opens a widget flow with my timeslot and ticket(s) selected at checkout

Unfortunately, I ran out of time -- this script is only about 2/3's completed.  There are various TODO comments throughout

"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import sys

def send_chars(keys_to_send):
	actions = ActionChains(driver)	# either 'abc' or Keys.TAB
	actions.send_keys(keys_to_send)
	time.sleep(2)
	actions.perform()

passed = True												# global pass fail.  Stays True only if all tests pass
#region_names = ["Costa Rica", "Bahamas", "Belize"]			# the three test loctions/region names
region_name = "Belize"
star_line_80 = "\n" + "*" * 80 + "\n" + "*" * 80 + "\n"		# a text line designed to help demark locations in the results log
star_line_40 = "\n" + "*" * 40 + "\n"						# a text line designed to help demark indie tests in the results log

try:				# Can the file be opened?
	f = open("book_activity.txt", "a+")					# open the test log in append mode with handle 'f'
except IOError:			# No!  The file could not be opened.
	print("Couldn't open book_activity.txt", f)
	sys.exit()			# Die.

# f.write("\n\n\n\nThis test run was executed on {}.\n".format(time.ctime(time.time())))		# log the time
driver = webdriver.Firefox()							# set up the browser driver
driver.implicitly_wait(5)								# wait up to 5 seconds for web page elements to be drawn
driver.get("http://www.peek.com")						# open the root web page

# f.write(star_line_80)
# f.write("Tests for region name = {}.".format(region_name))			# note region name in the log
# f.write(star_line_80)

# ######################################################################################
# # Beginning of test to verify the entered geographical area returns the correct related activities
# ######################################################################################
# f.write(star_line_40)
# f.write("Test for initial region search.")				# note the test in the log
# f.write(star_line_40)

gs_input = driver.find_element_by_class_name("geosuggest__input")		# locate the inital search box element
gs_input.clear()
gs_input.send_keys(region_name)							# type in the region name to search
gs_input.send_keys(Keys.RETURN)							# hit the return key a few times
time.sleep(2)
gs_input.send_keys(Keys.RETURN)
time.sleep(2)
gs_input.send_keys(Keys.RETURN)

# activity corresponds to the first activity displayed after searching a geo region
activity = driver.find_element_by_xpath('//div[@class="components-LazyImage-style---placeholder components-LazyImage-style---background components-ActivityRow-style---activityImage"]').click()
time.sleep(5)
try:
	calendar_exists  = driver.find_element_by_xpath('//div[@class="containers-Activities-BookingBlock-style---bookingTitle text-center padding-sm-v"]')
except:
	f.write("Cannot find the activity's calendar widget.\nTest FAILED!")
	sys.exit()
print("Found the activity's calendar widget.\nTest passed.")

driver.execute_script("window.scrollBy(0, 700);")
date = driver.find_element_by_xpath('//span[@class="calendarDay    selected available"]')		# might not be working...

try:
	min_book_req = driver.find_element_by_class_name("padding-md-bottom")
except:
	pass
print("min_book_req:", min_book_req.text)
match = re.search('(\d+)', min_book_req.text)			
number_to_increase = match.group(1)	
print("number_to_increase:", number_to_increase)
#book_now = driver.find_element_by_xpath('//div[@class="padding-md"]')
increase = driver.find_element_by_class_name("fa-plus")
time.sleep(3)
for i in range(int(number_to_increase) - 1):
	increase.click()

	# TODO: the try/except below is meant to check for when the minimum person booking requirements were met
	try:
		#min_book_req = driver.find_element_by_class_name("padding-md-bottom")
		pass
	except:
		pass
print("Can no longer find the 'You need to book at least x tickets to meet the minimum required' message.  Good.")
# the following loop will increase the requested ticket count to a ridiculous level, which should be refused
for i in range(100):
	increase.click()
# TODO: now have to check that there's text for, "No availability for the date and ticket amount you have chosen",
# then log results

# this loop takes the ticket count back down to a reasonable level
decrease = driver.find_element_by_class_name("fa-minus")
for i in range(100):
	decrease.click()


book_now = driver.find_element_by_xpath('//div[@class="padding-md"]').click()
time.sleep(5)

# the following lines step through the contact info form
book_flow = driver.find_element_by_xpath('//div[@class="components-BookingFlowModal-style---bookingFlowModal"]').click()
send_chars(Keys.TAB)
send_chars('First')			# enter first name
send_chars(Keys.TAB)
send_chars('Last')			# enter last name
send_chars(Keys.TAB)
send_chars(Keys.TAB)
send_chars('510-849-1619')
send_chars(Keys.TAB)
send_chars('a@b.com')
# clicking on this element goes to the final booking data, including the timeslot and ticket info
book_flow = driver.find_element_by_xpath('//div[@class="components-BookingFlowModal-style---bookingFlowModal"]').click()

# TODO: now have to grab the elements containing the timeslot and ticket info, compare them to expected values and log results...

