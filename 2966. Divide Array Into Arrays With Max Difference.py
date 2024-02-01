class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        temp=[nums[0]]
        l,r=-3,-3            
        while(r<len(nums)):
            l,r=l+3,l+4
            temp=[nums[l]]
            while(r-l<3):
                if(nums[r]-nums[l]>k):
                    return []
                else:
                    temp.append(nums[r])
                    r+=1
            ans.append(temp)
        return ans
