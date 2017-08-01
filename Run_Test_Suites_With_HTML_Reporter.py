import unittest
import HTMLTestRunner
import os
from Test_Audio_Files import AudioFileTests
from Test_Time_Outs import TimeOutTestCase
from Test_URLs import URLTestCases
from Test_Takes import Testing_For_Unavailability
from Test_Invalid_Fields import DatabaseTests
from Test_Transitions import PageTransitionTestCases

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
audio = unittest.TestLoader().loadTestsFromTestCase(AudioFileTests)
time_out = unittest.TestLoader().loadTestsFromTestCase(TimeOutTestCase)
url = unittest.TestLoader().loadTestsFromTestCase(URLTestCases)
takes = unittest.TestLoader().loadTestsFromTestCase(Testing_For_Unavailability)
database = unittest.TestLoader().loadTestsFromTestCase(DatabaseTests)
transition = unittest.TestLoader().loadTestsFromTestCase(PageTransitionTestCases)

# create a test suite combining search_text and home_page_test
#this one for local database tests
#test_suite = unittest.TestSuite([database, url, transition])
#this one for rasberry pi
#test_suite = unittest.TestSuite([audio])
test_suite = unittest.TestSuite([takes])
# open the report file
outfile = open(dir + "/TestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Front End Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
