"""
Check words with typos: Given two strings, check if they are one typo
(or zero typos) away. Three types of typos: insert a character, remove a character
or replace a character.
one typo -> True
zero typos -> False

pale, ple -> one typo
pale, pale
pale, bake
"""


def calculate_tipos(str1, str2):
	count = 0 
	# determine if string 2 is a subset of string 1
	if(len(str1) > len(str2)):
	 # str1 = pale, str2 = ple
		for i in range(len(str2)):   # ple
			if (str2[i] in str1):
				count = count + 1    # count = 3  length of string 1 = 4
		# calculate one typo
		if len(str1)-count == 1 or len(str1)-count == -1:
			print("true")
		else:
			print("false")

	# determine if string 1 is a subset of string 2
	elif(len(str2) > len(str1)):
		for i in range(len(str1)):
			if (str1[i] in str2):
				count = count + 1
		# calculate one typo
		if len(str2)-count == 1 or len(str2)-count == -1:
			print("true")
		else:
			print("false")

	# if both strings have the same length: pale, bake => b/p and l/k

	else:
		for i in range(len(str1)):
			# check if count is 2 or more, that is, two or more typos
			if(str1[i] not in str2):
				count = count + 1
		if (count >= 2):
			print("false")
		else:
			print("true")

	

# Main function

# prompt user to enter both strings:
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

calculate_tipos(string1, string2)


"""
Complexity of Algorithm:
Since we are comparing two strings of length n, then the time to access the entire length
of each string is O(n), giving it a complexity of O(n^2), that is quadratic. Spatial 
complexity depends on the length of each string.
"""