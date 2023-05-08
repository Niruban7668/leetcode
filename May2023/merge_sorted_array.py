class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while(m<len(nums1)):
            nums1.pop(m)
        for k in nums2: 
            nums1.append(k)
        if(m==0):
            j=0
            while j < len(nums1):
                if nums1[j] == 0:
                    nums1.pop(j)
                else:
                    j+=1

        nums1.sort()