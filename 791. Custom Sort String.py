class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_key = {}
        str = ""
        for char in s:
            if char in hash_key:
                hash_key[char] += 1
            else:
                hash_key[char] = 1
        
        for char in order:
            if char in hash_key:
                str += char * hash_key[char]            
                del hash_key[char]
                
        for key,value in hash_key.items():
            str += key * value
            
        return str

solution = Solution()
res = solution.customSortString("cba","abcd")        
print(res)
