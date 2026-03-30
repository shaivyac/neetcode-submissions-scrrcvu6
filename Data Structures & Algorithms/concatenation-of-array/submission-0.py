class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        counter =0
        for i in range(2*n):
            if i==n:
                counter=0
            ans.append(nums[counter])
            counter+=1
        return ans