'''
Problem
Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates 
n-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates
will be [2, 3, 6, 9].

Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates
will be [2, 11].

Idea
Because of the 'don't use extra space', we can't use something
like a dictionary or create a new array to store each unique 
element. That means we will have to do in place deletions.
The time complexity of deleting index i from a list of n 
elements is O(n - i).

Since the array is sorted, any dups will be contiguous.
Keep a pointer on an elem and search the rest of the list
for duplicates of this value. 
Do this until the left pointer != right pointer
'''

def remove_duplicates(arr):
	# index of next non duplicate
	next_non_dup = 1
	i = 1
	while (i < len(arr)):
		# 
		if arr[next_non_dup - 1] != arr[i]:
			arr[next_non_dup] = arr[i]
			next_non_dup += 1
		i += 1
	return next_non_dup


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()
