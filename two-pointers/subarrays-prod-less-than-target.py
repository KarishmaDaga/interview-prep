'''
Problem Statement #

Given an array with positive numbers and a 
target number, find all of its contiguous 
subarrays whose product is less than the target
number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays
whose product is less than the target.

Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], 
[6, 5] 
Explanation: There are seven contiguous subarrays 
whose product is less than the target.

Idea
- note: contiguous subarray also includes single
values 
- keep track of current subarray product
- two pointers, sliding window vibe
- when product < target, append arr[left:right]
- shrink window when product >= target
- expand window and grow subarray list while
product is less than target
- don't think my idea for the subarray list is 
the best/correct
'''
def find_subarrays(arr, k):
	if arr is None or k < 1:
		return -1

	curr_product = 1
	result = []
	window_start = 0

	# expanding window while product is 
	# less than target
	for window_end in range(len(arr)):
		# calculate curr_prod
		curr_prod *= arr[window_end] if arr[window_end] != 0
		# shrink window
		while curr_prod >= k and window_start < len(arr):
			# remove window start from product
			curr_prod /= arr[window_start]
			window_start += 1
		# add subarrays to result
		if arr[window_end] < k:
			result.append([arr[window_end]])
			result.append(tmp)
	return result



