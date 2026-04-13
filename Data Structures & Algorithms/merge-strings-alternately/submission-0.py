class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        len3 = min(len1,len2)
        word3 = ""
        for i in range(len3):
            word3= word3+word1[i]+word2[i]
            #print(word3)
        word3 = word3+word1[len3:]+word2[len3:]
        return word3

            
            

