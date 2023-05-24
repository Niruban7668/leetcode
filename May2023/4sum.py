class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums=sorted(nums)
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                l=len(nums)-1
                while k<l:
                    summ=nums[i]+nums[j]+nums[k]+nums[l]
                    if summ==target:
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                        k=k+1
                        l=l-1
                    elif summ>target:
                        l=l-1
                    else:
                        k=k+1
        return res

#https://leetcode.com/problems/4sum/description/
#medium