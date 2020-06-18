"""Partial permutation: Given two strings, write a method to decide if one is a partial
permutation of the other. Consider a partial permutation if:
- The first letter hasn't changed place;
- If the word has more than 3 letters, up to 2/3 (<=67%) of the letters have changed place

possible solution:
1) if arr1[i] is different from arr2[i], count++
At the end, do the following: count/length(array). If this equals 2/3, then return true

"""


def partial_permutation(str1, str2):
	count = 0     # count the number of positions in which letters have changed in both strings
	if (str1[0] == str2[0] and len(str1)==len(str2) and len(str1)>=3):
		for i in range(len(str1)):
			# if letters have changed at some position in both arrays, count that position
			if str1[i] != str2[i]:
				count = count + 1      
		# calculate the ratio of letters changed
		partial_perm = (count / len(str1)) * 100
		# if the ratio of letters changed is less than or equal to 2/3, then partial permutation
		if (partial_perm <= ((2/3)*100)):
			print("true: partial permutation")
		else:
			print("false: not partial permutation")
	else:
		print("false: not partial permutation")

# Main function

# prompt user to enter both strings:
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

partial_permutation(string1, string2)


"""
Complexity of Algorithm:
Since we are comparing two strings of length n, then the time to access the entire length
of each string is O(n), giving it a complexity of O(n^2), that is quadratic. Spatial 
complexity depends on the length of each string.
"""