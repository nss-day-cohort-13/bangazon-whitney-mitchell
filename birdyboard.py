import pickle
import uuid
import sys

class Birdy:

	def __init__(self, u_file, c_file):
		# init object
		self.users_file = u_file
		self.chirps_file = c_file
		# deserialize users and chirps
		try:
			self.deserialize_users(self.users_file)
		except EOFError:
			self.all_users = []

		try:
			self.deserialize_chirps(self.chirps_file)
		except EOFError:
			self.all_chirps = []

		# display app title
		title = self.title()
		# print(self.all_users)

	def title(self):
		print("#########################################")
		print("##      ~~~~~Birdyboard~~~~~           ##")
		print("#########################################")

###### MAIN MENU ######
	def menu(self):
		# show menu of options, read user input response and use it to call appropriate method
		self.options = "1. New User Account\n2. Sign In\n3. View Chirps\n4. Public Chirp\n5. Private Chirp\n6. Exit"
		print("Type the number of your chosen option:")
		print(self.options)
		choice = input("> ")

		try:
			if int(choice) > 0 and int(choice) < 7:

				if choice == "1":
					print("What is your full name?")
					self.user_name = input("> ")
					print("What would you like your screenname to be?")
					self.screen_name = input("> ")
					new_user = self.new_user(self.user_name, self.screen_name)
					print("Cool, {0}. Now what do you want to do?".format(self.screen_name))
					self.menu()

				elif choice == "2":
					print("Type the number next to your screenname:")

					signed_in_user = self.sign_in()
					# signed_in_user is the return value from the sign_in method, the user's screenname
		#########TAKE OUT THIS PRINT STMT eventually
					# print("SIU", signed_in_user)
					print("Hey, {0}! What next?".format(signed_in_user))
					self.menu()

				elif choice == "3":
					print("3")
				elif choice == "4":
					print("4")
				elif choice == "5":
					print("5")
				elif choice == "6":
					self.serialize_users(self.users_file)
					exit()
			else:
				print("\nChoose an option. Type 1, 2, 3, 4, 5, or 6.\n")
				self.menu()

		except ValueError:
			print("\nChoose a number, 1-6.\n")
			self.menu()

###### NEW USER: OPTION 1 ######
	def new_user(self, user_name, screen_name):
		# User choice 1: create new user, save fullname and screenname.
		# Save to CSV. Then show menu (3-6).
		self.user = {"uid": uuid.uuid4(),
								"username": user_name,
								"screenname": screen_name}
		self.all_users.append(self.user)
		self.serialize_users(self.users_file)
		return self.user

###### SIGN IN: OPTION 2 ######
	def sign_in(self):
		# User choice 2: select from a menu of users, serving as a sign-in. Then show menu (3-6).

		user_tuple_list = []

		i = 1
		for a in self.all_users:
			print("{0}. {1}".format(i, a["screenname"]))
			user_tuple_list.append((i, a))
			i += 1

		self.sign_in_choice = input("> ")


		for tup in user_tuple_list:

			if str(tup[0]) == self.sign_in_choice:
				user_dictionary = tup[1]
				screenname_signed_in = user_dictionary["screenname"]
				return screenname_signed_in

		else:
			print("You should type a number. Start over.")
			self.menu()

###### VIEW CHIRPS: OPTION 3 ######
	def view_chirps(self):
		# User choice 3: select which chirps to view - private or public.
		# Then, give option to select a chirp. Selecting shows that chirp"s
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


###### SERIALIZATION TASKS ######
	def serialize_users(self, filename):
		# saves users to disk
		with open(self.users_file, "wb+") as u:
			pickle.dump(self.all_users, u)

	def deserialize_users(self, filename):
		# opens users from disk and loads into memory. On error, creates the file.
		try:
			with open(self.users_file, "rb") as u:
				self.all_users = pickle.load(u)

		except FileNotFoundError:
			self.all_users = []
		# print(self.all_users)
		return self.all_users

	def serialize_chirps(self, filename):
		with open(self.chirps_file, "wab+") as c:
			pickle.dump(self.all_chirps, c)
			print(self.all_chirps)

	def deserialize_chirps(self, filename):
		try:
			with open(self.chirps_file, "rb") as c:
				self.all_chirps = pickle.load(c)

		except FileNotFoundError:
			self.all_chirps = []


###### RUN IT ######
if __name__ == "__main__":
	birdy = Birdy("users.csv", "chirps.csv")
	birdy.menu()
