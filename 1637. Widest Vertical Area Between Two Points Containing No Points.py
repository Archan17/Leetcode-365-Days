class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted([x for x,y in points])
        return max([x[i+1]-x[i] for i in range(len(x)-1)])
        
