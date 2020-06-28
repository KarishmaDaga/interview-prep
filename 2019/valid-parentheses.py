# https://leetcode.com/problems/valid-parentheses/

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        base case is if input str is empty.
        
        We can store the bracket characters in a hash map (dictionary) and use a stack to determine if the string is balanced.
        If we encounter an opening bracket, we add it to the stack. If we encounter a closing bracket, then we will check the stack
        to see if it matched the top bracket. If it does, we can pop that value and continue. If it does not, we have an unbalanced string.
        If we reach the end of the string and the stack is non empty, then we have an unbalanced string.
        
        """
        # base case: empty input string
        if s == None:
          return True
        
        # create dict with bracket values
        mapping = { ')':'(', ']':'[', '}':'{' }
        
        # create empty stack. I will implement it as a array.
        stack = []
        
        for char in s:
          # encounter a opening bracket
          if char in mapping.values():
              # add to stack
              stack.append(char)
          # encounter closing bracket
          elif char in mapping.keys():
              # check if stack is already empty or closing bracket 
              # does not match opening bracket in stack
              if stack == [] or mapping[char] != stack.pop():
                  return False
          # handle case if char is not a bracket
          return False
        # returns true if stack is empty (balanced string) or false if unbalanced
        return stack == []
            
       
# Leetcode solution:

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
        
        
        
        
        
        
        
        
        
