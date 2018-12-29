# 347: Top K Frequent Elements - Medium

# Given a non empty array of integers, return the k most frequent elements
# Note:
# assume k is always valid, 1<= k <= number of unique elements
# complexity must be better than O(nlogn) where n = array size

# if len(nums) == 1 return nums[0] 

# can create hashmap of element to occurrences? this would work for k = 1, 
# need to use a max heap ordered by frequency

class Solution:
	def topKFrequent(self, nums, k):
	
	count = collections.Counter(nums) # counter( {1:3, 2:2, 3:1})
	return heapq.nlargest(k, count.keys(), key = count.get)

