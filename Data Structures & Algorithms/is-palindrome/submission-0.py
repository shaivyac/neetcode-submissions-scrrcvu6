class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('Z') or ord('0')<=ord(i)<=ord('9'):
                string +=i 
        string=string.lower()
        #print(string)
        i =0
        j = len(string)-1
        while i<j:
            if string[i]==string[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        