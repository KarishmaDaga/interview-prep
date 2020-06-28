

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Iterate through string, adding values to a sum var. If current value is less than the next value, add the negative of the curr to 
        sum. This way I don't have to keep track of curr or next.
        """
        # create hash map storing alphabet values
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
        # init sum of the letters
        sum = 0
        
        # return sum (0) if given string is empty
        if s == "":
            return sum
            
        # iterate through string
        for i in range(0, len(s)-1):
        
        # check if next value is greater than current
            if roman.get(s[i]) < roman.get(s[i+1]):
                sum -= roman.get(s[i])
            else:
                sum += roman.get(s[i])
        # return last value since the condition does not apply to the last value
        return sum + roman.get(s[-1])
