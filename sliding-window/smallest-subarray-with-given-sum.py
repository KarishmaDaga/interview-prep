'''
Problem
Given an array of positive numbers and a positive number 
‘S’, find the length of the smallest contiguous subarray 
whose sum is greater than or equal to ‘S’. Return 0, if no 
such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than 
or equal to '7' is [5, 2].

Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than
or equal to '7' is [8].

Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than
or equal to '8' are [3, 4, 1] or [1, 1, 6].

Idea
This is a problem with a non-fixed window size! We are 
optimizing for the smallest subarray length, so we will
keep track of the min_length and update against it with 
subarrays we find that have a sum of S or more.
- expand window: until the current sum is greater than or equal
to S
- shrink window: until the current sum is back to being less
than S. we can reuse the window sum by simply subtracting 
the start of the window
'''

def smallest_subarray_sum(arr, s):
	# check valid args
	if arr is None or s < 1:
		return -1
	curr_sum = 0
	window_start = 0
	min_len = 0

	# expand window
	for window_end in range(len(arr)):
		curr_sum += arr[window_end]

		# shrink window
		while (curr_sum >= s):
			# update min length
			min_len = min(min_len, window_end - window_start + 1)
			# slide window forward
			curr_sum -= arr[window_start]
			window_start += 1
	return min_len

def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()