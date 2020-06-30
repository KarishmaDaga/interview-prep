'''
Problem Statement #

Given an array of unsorted numbers, find all 
unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
[-3, -2, -1, 0, 1, 1, 2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], 
[-1, 0, 1]
Explanation: There are four unique triplets 
whose sum is equal to zero.

Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets 
whose sum is equal to zero.

Idea
- variation of target sum where k = 0 and 
x + y + z = 0
- for each current value c, we're looking for 
x + y + c = 0 ==> c = -x - y
- note: need all unique triplets, skip dup #s
'''

def search_triplets(arr):
	arr.sort()
	triplets = []
	for i in range(len(arr)):
		if i > 0 and arr[i] == arr[i-1]: #duplicate
			continue
		_search_pair(arr, -arr[i], i+1, triplets)
	return triplets

def _search_pair(arr, target_sum, left, triplets):
	right = len(arr)-1
	while (left < right):
		curr_sum = arr[left] + arr[right]
		if curr_sum == target_sum: # found triplet
			triplets.append([-target_sum, arr[left], arr[right]])
			left += 1
			right -= 1
		while left < right and arr[left] == arr[left - 1]:
			left += 1
		while left < right and arr[right] == arr[right + 1]:
			right -= 1
	elif target_sum > curr_sum:
		left += 1 # need pair with bigger sum
	else:
		right -= 1 # need pair with smaller sum

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()