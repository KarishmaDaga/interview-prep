# 347: top k most frequent elements 
# Given a non empty array of integers, return the k most frequent elements.
# A max heap/priority queue ordered by frequency makes sense here. 

class Solution:
    def topKFrequent(self, nums, k):
        # count frequency of elements in nums
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)

