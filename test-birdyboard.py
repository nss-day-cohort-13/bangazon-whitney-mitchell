import unittest
import pickle
import sys
from birdyboard import *

# Test returns, test core logic/functionality
# "Does the app break if this thing breaks?"

class Test_birdy(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.birdy = Birdy()

	def test_new_user_creation(self):
		pass

	def test_select_user_selects_correctly(self):
		pass

	def test_view_chirps(self):
		# This will probably be broken into several functions,
		# I'm just not sure yet how I'll do this testing.
		# Prob test that private chirps are really private, public are public...
		pass

	def test_public_chirp_saves_where_it_should(self):
		# Just unclear on where it will save right now,
		# but I assume the test-chirps.csv file.
		pass

	def test_private_chirp_saves_where_it_should(self):
		# Just unclear on where it will save right now,
		# but I assume the test-chirps.csv file.
		pass



if __name__ =='__main__':
		unittest.main()
