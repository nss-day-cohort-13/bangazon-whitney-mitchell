import pickle
import sys

class Birdy:

	def __init__(self):
		pass
		title = self.title()
		# init object

	def title(self):
		print("#########################################")
		print("##      ~~~~~Birdyboard~~~~~           ##")
		print("#########################################")

	def menu(self):
		# show menu of options, read user input response and use it to call appropriate method

		self.options = "1. New User Account\n2. Select User\n3. View Chirps\n4. Public Chirp\n5. Private Chirp\n6. Exit"
		print(self.options)
		choice = input("> ")

		try:
			if int(choice) > 0 and int(choice) < 7:
				if choice == "1":
					print("1")
				elif choice == "2":
					print("2")
				elif choice == "3":
					print("3")
				elif choice == "4":
					print("4")
				elif choice == "5":
					print("5")
				elif choice == "6":
					exit()
			else:
				print("\nChoose an option. Type 1, 2, 3, 4, 5, or 6.\n")
				self.menu()

		except ValueError:
			print("\nChoose a number, 1-6.\n")
			self.menu()

	def new_user(self):
		# User choice 1: create new user, save fullname and screenname.
		# Save to CSV. Then show menu (3-6).
		pass

	def select_user(self):
		# User choice 2: select from a menu of users, serving as a sign-in. Then show menu (3-6).
		pass

	def view_chirps(self):
		# User choice 3: select which chirps to view - private or public.
		# Then, give option to select a chirp. Selecting shows that chirp's
		# thread, and options to reply or go back.
		pass

	def public_chirp(self):
		# User choice 4: create chirp that can be viewed by everyone, when they choose menu option 3.
		# Display chirp appropriately. Send to chirps.csv
		pass

	def private_chirp(self):
		# User choice 5: select from menu of users, then create a chirp that only they can see.
		# Maybe will endup inheriting fron public chirp?
		# Display chirp appropriately. Send to chirps.csv
		pass



if __name__ == "__main__":
	birdy = Birdy()
	birdy.menu()
