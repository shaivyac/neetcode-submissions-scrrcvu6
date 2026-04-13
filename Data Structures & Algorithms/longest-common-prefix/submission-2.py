class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str=""
        length=201
        common=""
        for i in strs:
            if len(i)<length:
                length= len(i)
                shortest_str=i

        for l in range(length+1):
            common_b = True
            for i in strs:
                #print(shortest_str[:l],i[:l])
                if shortest_str[:l]!=i[:l]:
                    common_b= False
            if common_b==False:
                common=shortest_str[:l-1]
                break
            else:
                common=shortest_str[:l]

        return common


                    
        


            
