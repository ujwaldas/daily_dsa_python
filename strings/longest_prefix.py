class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_common = strs[0]
        for word in strs[1:]:
            for i in range(len(word),-1,-1):
                if word[:i] == longest_common[:i]:
                    longest_common = longest_common[:i]
                    break
        return longest_common


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))