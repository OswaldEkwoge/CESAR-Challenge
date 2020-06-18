""" 
Replacing characters in place
Given an array of characters, write a method to replace all the spaces with "&32".
"""
# function to replace blank space with required character

def replace_space(array):
	new_array = array.replace(" ", "&32")
	print(new_array)

# Main function
# Prompt user to enter string:
array = input("Enter your string: ")
#array = "User is not allowed"
replace_space(array)

"""
Complexity of algorithm
This algorithm is linear, presenting a complexity of O(n), because it runs the entire length
of the string, looking for an empty space and replacing them with "&32. Even though, it has
a linear complexity, the use of memory differs with respect to to the amount of empty space
to be replaced with &32. For instance, the length of the string, "User is not allowed" is 19
while the length of "User&32is&32not&32allowed" is 25.
"""