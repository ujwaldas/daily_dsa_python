# LeetCode Problem: Valid Anagram
# Author: Rancid_engineer
# 242. Valid Anagram
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettorDict = {}
        if(len(s) != len(t)):
            return False
        for letter in s:
            lettorDict[letter] = lettorDict.get(letter,0)+1
        for letter in t:
            if letter in lettorDict and lettorDict[letter] != 0:
                lettorDict[letter] -= 1
            else:
                return False
        return True
