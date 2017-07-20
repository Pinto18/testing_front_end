import unittest
import HTMLTestRunner
import os
from Integration_Tests import AudioFileTests

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
audio = unittest.TestLoader().loadTestsFromTestCase(AudioFileTests)
#home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([audio])

# open the report file
outfile = open(dir + "/TestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Front End Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)