# Hello there everybody! I am going to leave this for you. Think if it as a bit of a "guide".
# It will be some somewhat of a list of common definitions, skills, common algorithms... When
# learning about each of these, please focus more on the logic and purpose behind setting up
# and programming an algorithm or solutions to a problem.


################################################################################
## Variables, Print Statements, Data Types, Casting, Concatenation, F Strings ##
################################################################################

# Variables are used to represent something. Some value, some object, some list, something...

first_name = "Kevin"             # Data Type: String
last_name = "Santos"             # Data Type: String
current_age = 30                 # Data Type: Int
height = [6,1]                   # Data Type: List
nationality = ["USA", "Brazil"]  # Data Type: List
current_temp = 98.6              # Data Type: Float
is_sick = False                  # Data Type: Boolean
roles = ["son",
         "fiance",
         "brother",
         "teacher",
         "dorm parent",
         "soccer player",
         "advisor",
         "coach"]

# We can print variables and see their values back on the screen
print(first_name)
print(current_age)

# We can use variables to be printed alongside text in a print statement
print("Hello there, my name is " + first_name + " " + last_name + " and I am " + str(current_age) + " years old") # Using Concatenation
print(f"Hello there, my name is {first_name} {last_name} and I am {current_age} years old." ) # Using 'F Strings'

# Concatenation is the addition of two strings. You cannot concatenate an int and a string 
speed = 20
units = "mph"
#print(speed + " " + units) # This will break when you run it so comment out if you want to run program successfully. Or cast str(speed) !

# Casting is done to change a Data Type to another Data Type if possible. This way, you can print out the statement above.
print(str(speed) + " " + units)

# We can check and see what the length is of a given variable or list with len(). Booleans, Integers and Floats have no length
print(len(first_name))   # My first name is 5 letters
print(len(last_name))    # My last name is 6 letters
print(len(nationality))  # I have two nationalities listed
print(len(roles))        # I have 8 roles listed


################################
############ LISTS #############
################################

# A list is meant to hold a set of values together in a way that allows them to be iterable. Executing some specific
# action for every item in a list is often useful! Or we can sort lists in numerous ways through many different methods
# as well.

# Lists are also objects. What properties or functions that any list should have associated with it in real
# life. A list has a length or number of items, you can add things to a list, you can remove things from a list,
# You can organize a list according to different rules, I can access items in any position...

# Here is how we can declare and give values to lists while printing them out to display the order. I am creating one
# list of string values and one list of int values.

animals = ["bear", "shark", "owl", "chameleon", "anaconda", "tucan"]
student_scores = [59,75,35,57,64,76,57,86,87,89,67,90,100,54]

# Access items in list based on position
print(animals[0]) # First item in list
print(animals[3]) # Fourth item in list
print(animals[-1]) # Last item in list
print(student_scores[2]) #Third student score in list

# Append value to end of list or insert into a specific position
animals.append("giraffe")
animals.insert(3, "dragon")

# Use pop() to remove an item from the end of a list. Or use remove to remove a specific value
last_animal_in_list = animals.pop()
print(f"The last animal ({last_animal_in_list}) was removed from list. Current List: {animals})")
animals.remove("dragon")
print(f"Dragon was removed. List should be back to original animals list")
print(animals)

# Print out max and min values. Numeric are straight forward. Strings are based on characters
print(min(animals))
print(max(animals))
print(min(student_scores))
print(max(student_scores))

# Creates a function that takes in a list and sorts low to high numeric values
def sort_low_to_high(list_of_values):
    # Empty list which will store sorted values
    ordered_list = []
    # Iterate through each number in list entered
    for temp_value in list_of_values:
        # Value is always not sorted to start
        inserted = False
        # For each number in the sorted list
        for i in range(len(ordered_list)):
            # If the number from our entered list is less than or equal value in sorted list
            if temp_value <= ordered_list[i]:
                # Enter that number in the place of the value in sorted list then change value to sorted
                ordered_list.insert(i, temp_value)
                inserted = True
                break
        # If not inserted then it is larger than all values, so add to end of list
        if not inserted:
            ordered_list.append(temp_value)
    # Since I would likely want to print the list or use it, I return the ordered list
    print(ordered_list)
    return ordered_list

# Calls function written above
sort_low_to_high(student_scores) 
sort_low_to_high(animals)

def average_scores(list_of_nums):
    total_sum = 0
    total_values = len(list_of_nums)
    average = None

    for num in list_of_nums:
        total_sum += num
    average = total_sum / total_values
    print(average.__round__(2))

average_scores(student_scores)
