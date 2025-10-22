class Solution:
    def groupAnagrams(self, strs):
        allFrequency = {}
        for word in strs:
            wordFrequency = {}
            for letter in word:
                wordFrequency[letter] = wordFrequency.get(letter,0)+1
            sorted_wordFrequency = sorted(wordFrequency.items())
            string_Frequency = str(sorted_wordFrequency)
            if string_Frequency in allFrequency:
                allFrequency[string_Frequency].append(word)
            else:
                allFrequency[string_Frequency] = [word]
        return allFrequency.values()
        
if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))