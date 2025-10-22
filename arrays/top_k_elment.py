class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1 
        i = 0
        sortedFreq = sorted(freq.items(),key=lambda x: x[1], reverse=True )
        returnList = []
        for key,value in sortedFreq:
            if i < k:
                returnList.append(key)
            else:
                break
            i += 1
        return returnList