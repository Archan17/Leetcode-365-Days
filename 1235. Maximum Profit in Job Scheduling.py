class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        @cache
        def max_profit(i):
            if i >= len(jobs):
                return 0
            prof1 = max_profit(i + 1)
            nxt = bisect_left(jobs, (jobs[i][1], 0, 0))
            prof2 = jobs[i][2] + max_profit(nxt)
            return max(prof1, prof2)
        
        jobs = sorted(zip(startTime, endTime, profit))
        return max_profit(0)
