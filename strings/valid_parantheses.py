# LeetCode Problem: Valid Parantheses
# Author: Rancid_engineer
# 20. Valid Parantheses
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        compareDict = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif not stack or stack[-1] != compareDict[char]:
                return False
            else:
                stack.pop()
        return not stack