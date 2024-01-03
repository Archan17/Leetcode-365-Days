class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        left, right = 0, 0
        count = 0
        while right != len(bank) - 1:
            right += 1
            if bank[right].count("1") != 0:
                count += bank[left].count("1") * bank[right].count("1")
                left = right
        return count
