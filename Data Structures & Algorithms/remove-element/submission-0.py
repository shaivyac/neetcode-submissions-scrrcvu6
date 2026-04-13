class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                #print("first",nums)
                nums[k]=nums[i]
                k+=1
                #print("result",nums)
        return k


        