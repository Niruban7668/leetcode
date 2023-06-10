class Solution:
    def min1(self,a,b,c) -> int:
        for i in range(0,c):
            if(b[i]==a):
                return b.index(b[i]) 
        return -1
    def max1(self,a,b,c) -> int:
        for i in range(c,len(b)):
            if(b[i]==a):
                return b.index(b[i]) 
        return -1
    def search(self, nums: List[int], target: int) -> int:
        mid=len(nums)//2
        if(target<nums[mid]):
            return self.min1(target,nums,mid)
        elif(target==nums[mid]):
            return nums.index(nums[mid])
        else:
            return self.max1(target,nums,mid)
        return -1

#https://leetcode.com/problems/binary-search/submissions/968064394/
#easy