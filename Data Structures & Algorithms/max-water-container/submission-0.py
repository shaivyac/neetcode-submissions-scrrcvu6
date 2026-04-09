class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0
        i=0
        j=len(heights)-1
        while i<j:
            diff = j-i
            square = min(heights[j],heights[i])*diff
            maxwater=max(square,maxwater)
            #print( heights[i],heights[j] , diff,square)
            if heights[j]>heights[i]:
                i+=1
            else:
                j-=1
        return maxwater
        