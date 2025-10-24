# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         palindrome = True
#         skip = False
#         right = len(s) - 1
#         if length == 0:
#             return palindrome
#         i = 0

#         while i <= length:
#             if s[i] == s[length]:
#                 palindrome = True
#             elif s[i] == s[length-1] and skip == False:
#                 palindrome = True
#                 skip = True
#                 length -= 1
#             elif s[i+1] == s[length] and skip == False:
#                 palindrome = True
#                 skip = True
#                 i += 1
#             else:
#                 palindrome = False
#                 break
#             i += 1
#             length -= 1
#         if palindrome == True:
#             return palindrome
#         length = len(s) - 1
#         i = 0
#         palindrome = True
#         skip = False
#         while i <= length:
#             if s[i] == s[length]:
#                 palindrome = True
#             elif s[i+1] == s[length] and skip == False:
#                 palindrome = True
#                 skip = True
#                 i += 1
#             elif s[i] == s[length-1] and skip == False:
#                 palindrome = True
#                 skip = True
#                 length -= 1
#             else:
#                 palindrome = False
#                 break
#             i += 1
#             length -= 1

#         print(palindrome)
#         return palindrome
        # for i in range(len(s)):
        #     elementRemoved = s[:i] + s[i+1:]
        #     if s[::-1] == s:
        #         print(s[::-1] == s)
        #         return True
        #     if elementRemoved == elementRemoved[::-1]:
        #         return True
        # return False
            

        class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        palindrome = True
        skip = False
        right = len(s) - 1
        if right == 0:
            return palindrome
        left = 0

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                left_skippedWord = s[:left] + s[left+1:]
                right_skippedWord = s[:right] + s[right+1:]
                return left_skippedWord == left_skippedWord[::-1] or right_skippedWord == right_skippedWord[::-1]
        return True