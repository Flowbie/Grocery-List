# Dolan, Austin
# ICS 110P Assignment 10
# November 7 2022
# Program displays my grocery list, user can add, remove, pop to next weeks grocery list, and finalize the list.


def print_list(grocery_list):
	# Create variable number to loop through to create numbered list
	number = 1
	# Loop through every item in grocery list and print after number
	for i in grocery_list:
		print(f"{str(number)}.", i)
		number += 1
	# Print number of items in grocery list
	print("This week's grocery list has ", len(grocery_list), " items.")

def main():
	# Variables
	prompt1 = "\nWhich command would you like to perform: (add, remove, save, or finalize) "
	prompt2 = "\nContinue working on your shopping list? (yes or no) "
	prompt3 = "\nDo you want to run the grocery list?\n  (yes or no) "
	prompt_add = "\nWhat do you want to add to the list? "
	prompt_remove = "\nWhat do you want to remove from the list? "
	prompt_save = "\nWhat do you want to remove from the list, and add to next weeks list? "

	# Grocery list and next weeks grocery list
	grocery_list = ['rice', 'dumplings', 'impossible meat', 'pork', 'tortillas', 'onions', 'cilantro']
	grocery_list_result = ', '.join(grocery_list)
	next_weeks_grocery_list = []
	print("Welcome to my grocery list application.\n")
	# Ask user their name and welcome to grocery application
	user_name = input("What's your name? In the future I will be able to store multiple grocery lists for everyone.\n").capitalize()
	# Detail functions that application can perform to user's grocery list
	print("\nMy list of functions includes:\n  Add: Add an item to the grocery cart\n  Remove: Removes an item from the grocery cart\n  Save:  Will remove an item from the grocery cart and add it to next weeks grocery list\n  Finalize:  This command will finalize your grocery list and display it for you in a numbered list.\n")
	try:
		run_grocery_list = input(f"\nOkay {user_name}, I can tell you what is currently on your grocery list and give you the chance to add or remove items before you go shopping.\nWork on your grocery list? (yes or no) ").lower()
		# Print out the grocery list seperated by ','
		print("The grocery list currently contains:", end = ' ')
		print(grocery_list_result)
		# If user says yes run the functions of the grocery list application
		while run_grocery_list != 'no':
			if run_grocery_list == 'yes':
				command = input(prompt1)
				# Add will add new item to grocery list
				if command == 'add':
					item = input(prompt_add)
					grocery_list.append(item)
					grocery_list_result = ', '.join(grocery_list)
					print("Your grocery list contains:", grocery_list_result)
					# run_grocery_list = input(prompt2)
				# Remove will remove item from grocery list
				elif command == 'remove':
					item = input(prompt_remove)
					grocery_list.remove(item)
					grocery_list_result = ', '.join(grocery_list)
					print("Your grocery list contains:", grocery_list_result)
					# run_grocery_list = input(prompt2)
				# Save will remove item from grocery list and add to next weeks grocery list
				elif command == 'save':
					item = input(prompt_save)
					grocery_list.remove(item)
					next_weeks_grocery_list.append(item)
					grocery_list_result = ', '.join(grocery_list)
					print("Your grocery list contains:", grocery_list_result)
					# run_grocery_list = input(prompt2)
				# Finalize will run print_list function which prints out the grocery list in a numbered list
				elif command == 'finalize':
					print_list(grocery_list)
					next_weeks_grocery_list_result = ', '.join(next_weeks_grocery_list)
					if len(next_weeks_grocery_list) > 0:
						print("The grocery list for next week contains the item('s): ", next_weeks_grocery_list_result)
					break
				# If user doesn't enter one of the commands I recognize tell them and prompt to enter again.
				else:
					print("That's not one of the commands I recognize!\n")
					run_grocery_list = input(prompt3)
			else:
				# If user doesn't enter yes or no tell them their response is invalid
				print(f"\n{run_grocery_list} is not a valid response.")
				run_grocery_list = input(prompt3)
	except ValueError as e:
		print("\nThat is not a valid response. Please try again.")
		print("Error:", end = " ")
		print(e)
	print("\nThank's for using my grocery list! Goodbye!")

main()

