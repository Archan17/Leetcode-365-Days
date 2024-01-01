class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie_cnt = 0
        cookie_dist = 0
        while cookie_dist < len(g) and cookie_cnt < len(s):
            if s[cookie_cnt] >= g[cookie_dist]:
                cookie_dist += 1
            cookie_cnt += 1
        return cookie_dist        

