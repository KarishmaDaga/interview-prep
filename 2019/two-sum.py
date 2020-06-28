# https://leetcode.com/problems/two-sum/

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9, 
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        I'm looking for indices of X, Y such that X + Y = target. If I have X, then I am searching for Y = target - X. 
        The brute force solutions would be two iterate through the list to find X, then find Y = target - X. 
        I could improve the efficiency by storing the values in nums and their indices in a hashmap.
        
        mapping: values -> indices
        base case: nums = []
        note: Y != X
        
        time complexity: O(n) to iterate through nums. O(n) to create hash map.
        """
        if nums == []:
            return nums
        else:
            # create hashmap
            mapping = {}
            
            # iterate through nums. if value you are at is Y = target - x, 
            for i in range(len(nums)):
                complement = target - nums[i]
                # check if complement exists in hash map
                if complement in mapping.values():
                    # return indices of complement Y and X
                    return mapping.get(complement), i
                else:
                    # not in mapping. add key-value pair (value, index)
                    mapping[nums[i]] = i
        
        
        
