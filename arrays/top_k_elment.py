# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         freq = {}
#         for num in nums:
#             freq[num] = freq.get(num,0) + 1 
#         sortedFreq = sorted(freq.items(),key=lambda x: x[1], reverse=True )
#         return [num for num,count in sortedFreq[:k]]


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
        
        return heapq.nlargest(k,freq.keys(),freq.get)
      
if __name__ == "__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))
