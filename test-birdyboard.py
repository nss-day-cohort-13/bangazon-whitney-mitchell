import unittest
import pickle
import sys
from birdyboard import *

# Test returns, test core logic/functionality
# "Does the app break if this thing breaks?"

class Test_birdy(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.birdy = Birdy("test-users.csv", "test-chirps.csv")

	# Do I need to test for deserialization? Error-handled, and it's in
	# the init, which makes me think I don't.
	def test_user_deserialization(self):
		pass

	# New user tests
	def test_new_user_creation(self):
		a_user = self.birdy.new_user("Bob Roberts", "RiotGrrl77")
		self.assertIs(a_user, self.birdy.user)
		self.assertEqual("Bob Roberts", a_user["username"])
		self.assertEqual("RiotGrrl77", a_user["screenname"])
		self.assertIsNotNone(a_user["uid"])
		self.assertIs(type(a_user), dict)

	# Sign in tests
	def test_sign_in_selects_correctly(self):
		self.sign_in_choice = 1
		self.assertEqual(self.birdy.sign_in(), "RiotGrrl77")
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
