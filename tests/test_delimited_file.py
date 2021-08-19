"""
Test if dapt.db.delimited_file.py is working correctly
"""


import csv
import os

import dapt

from tests.base import Database_test_base

class TestDelimitedFile(Database_test_base):

	def preflight(self):
		"""
        Testing items that should be ran before tests are ran.  This method returns a new
        class method for the test.

        Returns:
            The class instance which will be used for the unit test.
        """

		# Reset csv.  This is just used update the csv and reset it so interesting things happen.
		with open('test.csv', 'w') as f:
			writer = csv.DictWriter(f, fieldnames=['id', 'start-time', 'end-time', 'status', 'a', 'b', 'c'])
			writer.writeheader()
			writer.writerow({'id':'t1', 'start-time':'2019-09-06 17:23', 'end-time':'2019-09-06 17:36', 'status':'finished', 'a':'2', 'b':'4', 'c':'6'})
			writer.writerow({'id':'t2', 'start-time':'', 'end-time':'', 'status':'', 'a':'10', 'b':'10', 'c':''})
			writer.writerow({'id':'t3', 'start-time':'', 'end-time':'', 'status':'', 'a':'10', 'b':'-10', 'c':''})
	
		return dapt.db.Delimited_file('test.csv', ',')

	def postflight (self):
		"""
        Clean up after tests are ran.
        """

		os.remove('test.csv')

	def test_sup(self):
		assert True == True



