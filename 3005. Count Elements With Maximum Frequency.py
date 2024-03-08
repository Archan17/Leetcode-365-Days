class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        my_map = defaultdict(int)
        frequency = 0
        for num in nums:
            my_map[num] += 1
            frequency = max(frequency,my_map[num])      

        return sum([x for x in my_map.values() if x == frequency])    
