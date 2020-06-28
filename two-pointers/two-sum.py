'''
Problem
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers 
(i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target = 6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:

Input: [2, 5, 9, 11], target = 11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

Idea:
We could consider each element one by one and check the rest of
the elements to find a pair with the given sum. This would take
exponential time though given n elements i.e. o(n^2)

There are two efficient ways to approach this:
(1) Using the fact that the array is sorted, we can keep a left 
and right pointer at the beginning and end of the array. 
The left pointer will point to the smallest value in the array, 
and the right will point to the largest. Then, if the sum of the 
two pointers is larger than the target, we can try moving the right
pointer inwards to a smaller value. If the sum is less than the 
target, we can try incrementing the left pointer to a larger value.
We can keep doing this until the pointers either find a pair
or reach each other in the middle if they find no pair.
(2) This is useful in a non-sorted array. Since we're looking
for a pair (x, y) such that target = x + y, suppose the current
value we're at is x. Then we want to know if y = target - x is in
the array. We can use a dictionary = {current_val:index} to keep
track of values we've seen so that when we do the lookup for y,
we'll know if a target pair exists (or not).
'''

def two_sum_two_pointers(arr, target):
	'''
	Use two pointers to find a valid pair that sums to the
	target value. Returns the indices of the valid pair.
	:param: arr is the given arr of positive numbers
	:target: specific value a pair in the array must sum to
	'''
	left, right = 0, len(arr) - 1
	MISSING_TARGET = [-1, -1]

	while (left < right):
		curr_sum = arr[left] + arr[right]
		if curr_sum == target:
			return [left, right]

		if curr_sum > target:
			# need pair with smaller sum
			right_ptr -= 1
		elif curr_sum < target:
			# need pair with larger sum
			left_ptr += 1
	return MISSING_TARGET

def two_sum_one_pointer(arr, target):
	'''
	Find valid pair that sums to the target value. 
	Returns the indices of the valid pair. Use one pointer 
	to traverse the array and keep track of seen values 
	with a dictionary. 
	:param: arr is the given arr of positive numbers
	:target: specific value a pair in the array must sum to
	'''
	nums = {} # dict for seen elements
	MISSING_TARGET = [-1, -1]
	for i in range(len(arr)):
		# check if complement is in array, 
		complement = target - arr[i]
		if complement in nums:
			return [i, nums[complement]]
		else:
			# no pair, add current elem to dict
			nums[arr[i]] = i
	return MISSING_TARGET
			


def main():
	print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
	print(pair_with_targetsum([2, 5, 9, 11], 11))


main()