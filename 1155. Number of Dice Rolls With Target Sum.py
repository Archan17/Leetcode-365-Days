class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(None)
        def dp(remain, summ):
            if remain == 0:
                if summ == target: return 1
                return 0
            total = 0
            for i in range(1, k + 1):
                total += dp(remain - 1, summ + i)
            return total
        
        
        return dp(n, 0) % ((10**9) + 7)
                
