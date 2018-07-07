import random

date_ideas = ["Movies", "Walk in the Park", "Picnic", "Bowling", "Painting"]

def start():
        '''Prompts user with an opening menu asking for selection'''
        menu_select = ""
        while menu_select == "":
                menu_select = input("1 Get Date Idea, 2 Add a Date, 0 to Exit")
                if menu_select == "1":
                        print(random.choice(date_ideas))
                elif menu_select == "2": 
                        user_date = input("What would you like to add?")
                        date_ideas.append(user_date)
                
