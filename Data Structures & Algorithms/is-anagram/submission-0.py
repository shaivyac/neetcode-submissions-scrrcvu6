class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash ={}
        t_hash={}
        for i in s:
            if i in s_hash:
                s_hash[i] +=1
            else:
                s_hash[i] =1
        for j in t:
            if j in t_hash:
                t_hash[j] +=1
            else:
                t_hash[j] =1
        #print(t_hash , s_hash)
        if t_hash.keys() == s_hash.keys():
            #print(t_hash , s_hash)
            for k in t_hash:
                if t_hash[k] != s_hash[k]:
                    return False
        else:
            return False
        return True

                    
        
        