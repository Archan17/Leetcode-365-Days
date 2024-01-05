class Solution:
    def bs(self,l,r,lst,tr):
        pd=0
        while l<=r:
            mid=(l+r)//2
            if lst[mid]<tr:
                l=mid+1
            elif lst[mid]>tr:
                r=mid-1
                pd=mid
            else:
                pd=mid
                break
        return pd

    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        lst=[]
        for i in range(n):
            if len(lst)==0 or nums[i]>lst[-1]:
                lst.append(nums[i])
            else:
                x=self.bs(0,len(lst)-1,lst,nums[i])
                lst[x]=nums[i]
        return len(lst)
