class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            tuples = tuple(sorted(char for char in i))
            
            if tuples in anagram.keys():
                anagram[tuples].append(i)
            else:
                anagram[tuples] = [i]
        
        return list(anagram.values())