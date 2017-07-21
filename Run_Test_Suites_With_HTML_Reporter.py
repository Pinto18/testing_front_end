import unittest
import HTMLTestRunner
import os
from Test_Audio_Files import AudioFileTests
from Test_Zip_Files import ZipFileTestCases
from Test_Time_Outs import TimeOutTestCase
from Test_URLs import URLTestCases
from Test_Takes import Testing_For_Unavailbility

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
audio = unittest.TestLoader().loadTestsFromTestCase(AudioFileTests)
zip_file_test = unittest.TestLoader().loadTestsFromTestCase(ZipFileTestCases)
time_out = unittest.TestLoader().loadTestsFromTestCase(TimeOutTestCase)
url = unittest.TestLoader().loadTestsFromTestCase(URLTestCases)
takes = unittest.TestLoader().loadTestsFromTestCase(Testing_For_Unavailbility)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([audio, zip_file_test, time_out, url])

# open the report file
outfile = open(dir + "/TestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Front End Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
