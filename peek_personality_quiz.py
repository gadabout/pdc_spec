"""
Written by Michael McGreevy 071419

Feature: As a consumer visiting Peek.com I would like to take a personality quiz to cater search results to my preferences
* When completed, the quiz should provide a search form - when I search I should see my classification listed at the top of my search results

This script runs through two personality quizzes and logs the results in a file called, 'personality_quiz.txt', found in the same
directory as the script.

The lists nature_choices and insider_choices govern which picture selections the script should run.  One or the other of these lists will
be used, depending on whether the script is on the first or second iteration of the 'for i in range(2)' outer nested loop.  These two choice 
lists cover selecting all pictures.

The user story calls for a search to be performed after the quiz is completed.  I had difficulty finding a unique, keyboard accessible
web element corresponding to the search box.  Instead, I opted to leave the search box blank (a generic 'search'?) and just hit the search button.

TODO for improvements:
* Find a way to access the search box
* Include more error checking
* Add an outer nested loop to use all common web browsers/drivers

"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import sys

passed = True								# global pass/fail flag for all tests
star_line_80 = "\n" + "*" * 80 + "\n"		# a text line designed to help demark locations in the results log
nature_quote = "You love spectacular views and fresh air. All you need to be happy is the audio-visual therapy of being outdoors with a lush landscape before you."
insider_quote = "You're always in the know. You care about the authenticity in the details, be it in the contents of your cocktail or the music that you listen to."
nature_choices = [1, 0, 0, 1, 0, 0, 0, 0, 0]
insider_choices = [0, 1, 1, 0, 1, 1, 1, 1, 1]

try:				# Can the file be opened?
	f = open("personality_quiz.txt", "a+")					# open the test log in append mode with handle 'f'
except IOError:			# No!  The file could not be opened.
	writeit("Couldn't open personality_quiz.txt", f)
	sys.exit()			# Die.

f.write("\n\nThis test run was executed at {}.\n\n\n".format(time.ctime(time.time())))		# log the time

# each of the two iterations of this loop represents a seperate test run
for i in range(2):
	driver = webdriver.Firefox()							# set up the browser driver
	driver.implicitly_wait(5)								# wait up to 5 seconds for web page elements to be drawn
	driver.get("http://www.peek.com")						# open the root web page

	if i == 0:												# based on iteration, one set or the other of these parameters is used
		quote = nature_quote
		choices = nature_choices
		description = "Nature Lover Test"
	else:
		quote = insider_quote
		choices = insider_choices
		description = "Insider Test"
	f.write("{}{}".format(star_line_80, description))		# log the test iter demarcation and name
	# in the inner loop below, 'choice' is the web element that corresponds to the picture on the left or right
	for j in choices:
		if j == 0:
			choice = driver.find_element_by_xpath('//div[@class="components-PersonalityQuiz-QuizImagePicker-style---imageContainer margin-md-right"]').click()
		else:
			choice = driver.find_element_by_xpath('//div[@class="components-PersonalityQuiz-QuizImagePicker-style---imageContainer margin-xs-top"]').click()
		time.sleep(1)

	# search is the web element corresponding to the search button
	search = driver.find_element_by_class_name("components-Forms-Search-style---quizButton").click()
	# found_quote is the web element corresponding to the classification quote at the top of the consumer's displayed activities
	found_quote = driver.find_element_by_class_name("components-PersonalityQuiz-PersonalityResult-style---descriptionText")

	# this conditional is the crux of the script's pass/fail criteria.  If the quote is the correct one, pass.  Otherwise, fail
	if found_quote.text == quote:
		f.write("The classification quote displayed after taking the quiz is:\n{}\n\n".format(quote))
		f.write("This is correct.\n\n")
		f.write("Test iteration passed.\n\n")
	else:
		f.write("The classification quote displayed after taking the quiz is:\n*{}*\n\n".format(quote))
		f.write("However, the quote should have been:\n*{}*\n\n".format(quote))
		f.write("Test iteration FAILED!\n\n")
		passed = False

	driver.close()								# close the web browser for this region iteration
f.write("\n")

if passed == True:
	f.write("ALL TESTS PASSED.")
else:
	f.write("ONE OR MORE TESTS FAILED.")
f.write("\n\n\n")
f.close()	
