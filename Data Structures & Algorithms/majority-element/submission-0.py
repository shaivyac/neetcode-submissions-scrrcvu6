class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap.keys():
                hashmap[i]+=1
            else:
                hashmap[i]=1
        maxkey=0
        maxval =0
        for i in hashmap.keys():
            if hashmap[i]>maxval:
                maxval=hashmap[i]
                maxkey=i
        return maxkey

        