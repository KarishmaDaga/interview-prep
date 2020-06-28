# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while (left < right):
            # calculate area
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            # increment the pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_area
            
        
