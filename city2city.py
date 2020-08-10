# Created by:		Brad Arrowood
# Created on:		2020.02.15
# Last updated:		2020.02.17
# Script name:		city2city.py		
# Python version:	3.7.6
# Description:		After taking Quiz 2 of the edX "ColumbiaX: CSMM.101x Artificial Intelligence (AI)" course I wanted to
#			have some practice on the different search algorithms (BFS, DFS, and UCS) which were used.
#			Seeing as I've had much more practice working in Python and increasing the complexity of the scripts
#			I've written, I wanted to try making one to solve the problem using the search methods taught.
#			Below is my script to specifically solve this puzzle using the 3 algorithms taught.
#			I try to name my variables, lists, dictionaries, etc.. with useful names, comment A LOT, and explain
#			my thought process so others looking at my code or even myself reading back over it can easily understand it.

import os

cities = ['atlanta', 'boston', 'calgary', 'charleston', 'chicago', 'dallas', 'denver', 'duluth', 'el paso', 'helena',
    'houston', 'kansas city', 'las vegas', 'little rock', 'los angeles', 'miami', 'montreal', 'nashville', 'new orleans',
    'new york', 'oklahoma city', 'omaha', 'phoenix', 'pittsburgh', 'portland', 'raleigh', 'saint louis', 'salt lake city',
    'san francisco', 'santa fe', 'sault ste marie', 'seattle', 'toronto', 'vancouver', 'washington', 'winnipeg']

def cls():
    # Added to occationally clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def ask_type():
    # This function will list the 3 types of algorithms to choose from. Each option is listed with a choice number as its
    # its key in a dictionary. There is the added error checking code to ensure only a number from 1-3 is a valid intake.
    # This function then sets what type of algorithm to use as a variable and returns it
    
    end_flag = False
    while end_flag == False:
        cls()
        math_menu = {1: 'BFS', 2: 'DFS', 3: 'UCS'}
        print("\nList of search algorithms to choose from:")
    
        for key, value in math_menu.items():
            print(f"{key}. {value}")

        ask_search = input("\nInput the number for the type of algorithm you which to use: ")

        if ask_search:
            if (int(ask_search) > 0) and (int(ask_search) <= 3):
                search_type = math_menu.get(int(ask_search))
                end_flag = True
                
                return search_type

def ask_parameters():
    # This function is set to list the cities with corresponding number choice options. Unlike ask_type(), the cities are not
    # in a dictionary with the numbers paired with them. Instead they are generated (the same 1-36) each time the menu loads up.
    # Error checking code is also in place to ensure only a valid number can be accepted for both questions, the start and goal cities.
    # Also in error checking, you cannot choose the same cities as the start and goal options. If done the user is notified, 
    # the variable(s) are cleared, and the menu is reloaded
    # Once the cities are chosen, they are set to variables and returned.

    end_flag = False
    while end_flag == False:
        cls()
        city_count = 0
        menu = {}
        print("\nList of cities to choose from:")

        for city in cities:
            city_count+=1
            menu[city_count] = city
            print(f"{city_count}. {city.title()}")
        
        ask_start = input("\nInput the number for which city is the Starting location: ")

        if ask_start:
            if (int(ask_start) > 0) and (int(ask_start) <= city_count):
                ask_goal = input("Input the number for which city is the Goal location: ")
            
                if ask_goal:
                    if (int(ask_goal) > 0) and (int(ask_goal) <= city_count):
                        if int(ask_start) != int(ask_goal):
                            chosen_start_city = menu.get(int(ask_start))
                            chosen_goal_city = menu.get(int(ask_goal))
                            end_flag = True
                        
                            return chosen_start_city, chosen_goal_city
                        else:
                            print("\nYou've chosen the same city for both Start and Goal!")
                            input("Press Enter to go back and make a workable choice.")

def get_city(city_check):
    # This function is to hold the dictionaries labeled with each city.
    # Each dictionary contains the connection cities in key-value pairs with the distance cost tied to it.
    # A list is then made to contain all the dictionaries. When the function is called, the city dictionary to be pulled has its
    # index value from the main "cities" list pulled before having its equal index value within the list of dictionaries pulled.
    # For the BFS and DFS search types, only the keys are returned as a list while the UCS requires the key-value pairs.
    
    ATLANTA = {'charleston': 63, 'miami': 116, 'new orleans': 120, 'nashville': 67, 'raleigh': 96}
    BOSTON = {'montreal': 69, 'new york': 74}
    CALGARY = {'helena': 130, 'seattle': 118, 'vancouver': 100, 'winnipeg': 180}
    CHARLESTON = {'atlanta': 63, 'miami': 80, 'raleigh': 95}
    CHICAGO = {'duluth': 104, 'omaha': 142, 'pittsburgh': 81, 'saint louis': 104}
    DALLAS = {'houston': 46, 'el paso': 140, 'little rock': 74}
    DENVER = {'helena': 126, 'kansas city': 135, 'omaha': 130, 'phoenix': 128, 'salt lake city': 101, 'santa fe': 70}
    DULUTH = {'chicago': 157, 'helena': 150, 'omaha': 74, 'sault ste marie': 110, 'winnipeg': 103}
    EL_PASO = {'dallas': 140, 'los angeles': 191, 'santa fe': 65}
    HELENA = {'calgary': 130, 'denver': 126, 'duluth': 150, 'omaha': 174, 'salt lake city': 116, 'seattle': 189, 'winnipeg': 137}
    HOUSTON = {'dallas': 46, 'new orleans': 80}
    KANSAS_CITY = {'denver': 135, 'oklahoma city': 61, 'saint louis': 68}
    LAS_VEGAS = {'los angeles': 66, 'salt lake city': 89}
    LITTLE_ROCK = {'dallas': 74, 'nashville': 94, 'new orleans': 100, 'oklahoma city': 72, 'saint louis': 60}
    LOS_ANGELES = {'el paso': 191, 'las vegas': 66, 'phoenix': 109, 'san francisco': 100}
    MIAMI = {'atlanta': 116, 'charleston': 80, 'new orleans': 151}
    MONTREAL = {'boston': 69, 'new york': 99, 'sault ste marie': 193, 'toronto': 115}
    NASHVILLE = {'atlanta': 67, 'little rock': 94, 'raleigh': 128, 'saint louis': 85}
    NEW_ORLEANS = {'atlanta': 120, 'houston': 80, 'little rock': 100, 'miami': 151}
    NEW_YORK = {'boston': 74, 'montreal': 99, 'pittsburgh': 69, 'washington': 76}
    OKLAHOMA_CITY = {'kansas city': 61, 'little rock': 72, 'santa fe': 121}
    OMAHA = {'chicago': 142, 'denver': 130, 'duluth': 74, 'helena': 174}
    PHOENIX = {'denver': 128, 'los angeles': 109, 'santa fe': 85}
    PITTSBURGH = {'chicago': 81, 'new york': 69, 'toronto': 80, 'washington': 85}
    PORTLAND = {'salt lake city': 175, 'san francisco': 151, 'seattle': 44}
    RALEIGH = {'atlanta': 96, 'charleston': 95, 'nashville': 128, 'washington': 47}
    SAINT_LOUIS = {'chicago': 104, 'kansas city': 68, 'little rock': 60, 'nashville': 85}
    SALT_LAKE_CITY = {'denver': 101, 'helena': 116, 'las vegas': 89, 'portland': 175, 'san francisco': 156}
    SAN_FRANCISCO = {'los angeles': 100, 'portland': 151, 'salt lake city': 156}
    SANTA_FE = {'denver': 70, 'el paso': 65, 'oklahoma city': 121, 'phoenix': 85}
    SAULT_STE_MARIE = {'duluth': 110, 'montreal': 193, 'toronto': 90, 'winnipeg': 156}
    SEATTLE = {'calgary': 118, 'helena': 189, 'portland': 44, 'vancouver': 45}
    TORONTO = {'montreal': 115, 'pittsburgh': 80, 'sault ste marie': 90}
    VANCOUVER = {'calgary': 100, 'seattle': 45}
    WASHINGTON = {'pittsburgh': 85, 'raleigh': 47, 'new york': 76}
    WINNIPEG = {'calgary': 180, 'duluth': 103, 'helena': 137, 'sault ste marie': 156}
    
    city_dic = [ATLANTA, BOSTON, CALGARY, CHARLESTON, CHICAGO, DALLAS, DENVER, DULUTH, EL_PASO, HELENA, HOUSTON, KANSAS_CITY, LAS_VEGAS,
        LITTLE_ROCK, LOS_ANGELES, MIAMI, MONTREAL, NASHVILLE, NEW_ORLEANS, NEW_YORK, OKLAHOMA_CITY, OMAHA, PHOENIX, PITTSBURGH, PORTLAND,
        RALEIGH, SAINT_LOUIS, SALT_LAKE_CITY, SAN_FRANCISCO, SANTA_FE, SAULT_STE_MARIE, SEATTLE, TORONTO, VANCOUVER, WASHINGTON, WINNIPEG]

    dic_index = cities.index(city_check)
    
    if search_type != 'UCS':
        return list(city_dic[dic_index].keys())
    else:
        if city_check == 'atlanta':
            return ATLANTA
        elif city_check == 'boston':
            return BOSTON
        elif city_check == 'calgary':
            return CALGARY
        elif city_check == 'charleston':
            return CHARLESTON
        elif city_check == 'chicago':
            return CHICAGO
        elif city_check == 'dallas':
            return DALLAS
        elif city_check == 'denver':
            return DENVER
        elif city_check == 'duluth':
            return DULUTH
        elif city_check == 'el paso':
            return EL_PASO
        elif city_check == 'helena':
            return HELENA
        elif city_check == 'houston':
            return HOUSTON
        elif city_check == 'kansas city':
            return KANSAS_CITY
        elif city_check == 'las vegas':
            return LAS_VEGAS
        elif city_check == 'little rock':
            return LITTLE_ROCK
        elif city_check == 'los angeles':
            return LOS_ANGELES
        elif city_check == 'miami':
            return MIAMI
        elif city_check == 'montreal':
            return MONTREAL
        elif city_check == 'nashville':
            return NASHVILLE
        elif city_check == 'new orleans':
            return NEW_ORLEANS
        elif city_check == 'new york':
            return NEW_YORK
        elif city_check == 'oklahoma city':
            return OKLAHOMA_CITY
        elif city_check == 'omaha':
            return OMAHA
        elif city_check == 'phoenix':
            return PHOENIX
        elif city_check == 'pittsburgh':
            return PITTSBURGH
        elif city_check == 'portland':
            return PORTLAND
        elif city_check == 'raleigh':
            return RALEIGH
        elif city_check == 'saint louis':
            return SAINT_LOUIS
        elif city_check == 'salt lake city':
            return SALT_LAKE_CITY
        elif city_check == 'san francisco':
            return SAN_FRANCISCO
        elif city_check == 'santa fe':
            return SANTA_FE
        elif city_check == 'sault ste marie':
            return SAULT_STE_MARIE
        elif city_check == 'seattle':
            return SEATTLE
        elif city_check == 'toronto':
            return TORONTO
        elif city_check == 'vancouver':
            return VANCOUVER
        elif city_check == 'washington':
            return WASHINGTON
        elif city_check == 'winnipeg':
            return WINNIPEG

def bfs_dfs(start, goal, type):
    # Creates a list with the start city being the only thing in it, an empty output list which will fill as we loop, and
    # setting the flag loop up. To deal with repeats, we pop the first city from the path list, check to see if anything is
    # in the variable, then add a copy of it to the output list before comparing it to the goal city we're looking for.
    # If it is the goal city, we double check for any duplicate entries in the output list and remove them, we use indexing of the
    #   list and a loop to grab each city and convert using a title() then save it back to its same index place for a clean
    #   copy/paste when using the output. finally we output the resulting path, using ', ' as dividers, then end the flag loop
    # If the city isn't thegoal city, we set a couple empty lists, get the dictionary of the popped city, which returns a list
    #   we then sort alphabetically. Following this, we pull each city from the imported list to be compared to the output list and
    #   if the imported city isn't already on the list it is added to a filtered list. Once all imported cities are checked against
    #   this, the filtered list is added to the end of the path list so as to update the path list for the next while loop.
    
    # Since the code for the BFS and DFS functions was 99% identical save for 2 lines of code, i combined both search algorithms
    # into a single function and at the pop() and sort()/reverse() points it checks for which search type is being used.
    
    path = [start]
    output_path = []
    end_flag = False
    
    while end_flag == False:

        if type == 'BFS':
            popped_city = path.pop(0)
        elif type == 'DFS':
            popped_city = path.pop(-1)
        
        if popped_city:
            output_path.append(popped_city)
            
            if popped_city == goal:
                output_path = list(dict.fromkeys(output_path))
                listing_count = 0
                for listing in output_path:
                    output_path[listing_count] = listing.title()
                    listing_count+=1
                print(f"You answer path is: {', '.join(map(str, output_path))}\n")
                end_flag = True
            else:
                imported_cities = []
                filtered_list = []
                imported_cities = get_city(popped_city)
                
                if type == 'BFS':
                    imported_cities.sort()
                elif type == 'DFS':
                    imported_cities.reverse()
                
                for imported_city in imported_cities:
                    if imported_city not in output_path:
                        filtered_list.append(imported_city)
                        
            path = path + filtered_list

def ucs(start, goal):
    
    path = [start]
    output_path = []
    path_cost = 0
    end_flag = False
    
    popped_city = path.pop(0)
    imported_dics = get_city(popped_city)
    
    while end_flag == False:
        
        
        # popped_city = path.pop(0)
        
        key_max = max(imported_dics.keys(), key=(lambda k: imported_dics[k]))
        key_min = min(imported_dics.keys(), key=(lambda k: imported_dics[k]))
        print(key_max)
        print(key_min)
        # print(value_min)
        end_flag = True
    
"""
    needed to make a blockspace to put notes in
    
    for UCS it will require pulling both the connecting cities and their path cost values
    since the UCS algorithm doesn't rely on an alphabetical sorting, only incremental,
    we can't use a list to pop in and out of, but will need to use a dictionary and possible external var for total cost calc
    
    
    New Orleans, Houston, Little Rock, Atlanta, Dallas, Miami, Saint Louis, Oklahoma City, Charleston
    
    
    starting city is loaded and connecting cities to it are put into a list
    check to see if goal is in list
    a checkpoint pulls the lowest value and stores the key-value pair
    each city has their dictionaries pulled for connecting cities and path costs
    a checkpoint


    starting city has its dictionary pulled
    the returned key-value pairs are then split into 2 lists, cities and path cost. this is tier 1
    the lowest value from the value list is taken to be added to the path cost
    
    2 path cost value totals are stored:
        1 to hold the current lowest value from all loaded cities and 
        1 to separately check for a lower number from each expanded set of loaded cities


"""
        

########################################################################
##### START OF SCRIPT ##################################################

search_type = ask_type()
start_city, goal_city = ask_parameters()
cls()
print(f"\nYou chose the {search_type} algorithm.")
print(f"\nStart: {start_city.title()} \nGoal: {goal_city.title()}\n")

if (search_type == 'BFS') or (search_type == 'DFS'):
    bfs_dfs(start_city, goal_city, search_type)
elif search_type == 'UCS':
    ucs(start_city, goal_city)
