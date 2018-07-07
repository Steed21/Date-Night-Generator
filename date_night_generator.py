import random

date_ideas = ["option 1", "option 2", "option 3", "option 4", "option 5"]

def start():
	'''Prompts user with an opening menu asking for selection'''
	menu_select = ""
	while menu_select == "":
		print ("1 Get Date Idea, 2 Add a Date, 0 to Exit")
		'''0 may not exist in mobile app'''
		menu_select = input("Please make a selection")
		if menu_select == "1":
			print(random.choice(date_ideas))
		'''Allows user to add their own date idea to the original list'''
		elif menu_select == "2": 
			 user_date = input("What would you like to add?")
			 date_ideas.append(user_date)



