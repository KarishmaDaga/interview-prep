'''
Problem: 
Given an array of positive numbers and a positive number ‘k’, 
find the maximum sum of any contiguous subarray of size ‘k’.

Examples:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

Idea
We want to slide a window of size k along the array
and find the largest sum produced by one of these windows
Once we've reached a window of size k, we should keep track 
of the max sum we've seen so far and update against this value
with the current window's sum. 
- 'expand window': when the window size is less than k
- 'shrink window': when window size is greater than k

'''
def max_sum(k, arr):
	# set max sum to be none if invalid args are passed
	if k < 0 or arr is None:
		return 0

	# init
	max_sum = curr_sum = 0
	window_start = 0

	for window_end in range(len(arr)):
		# move window forward and increase sum as window expands
		curr_sum += arr[window_end]
		# if window is of size k, update the max_sum against the current
		if window_end + 1 >= k: # because of indexing
			max_sum = max(max_sum, curr_sum)
			# move window forward
			curr_sum -= arr[window_start]
			window_start += 1
	return max_sum

