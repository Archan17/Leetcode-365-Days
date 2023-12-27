class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        return sum(neededTime) - sum([
            max(g)[1] 
            for _, g in groupby(zip(colors, neededTime), itemgetter(0))]
        )
