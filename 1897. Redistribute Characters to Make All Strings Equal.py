class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp={}
        for word in words:
            for it in word:
                if it not in mp:mp[it]=1
                else:mp[it]+=1
        for i in mp:
            if mp[i]%len(words):
                return False
        return True
