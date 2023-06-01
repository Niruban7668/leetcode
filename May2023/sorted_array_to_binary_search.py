class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.constructBST(nums, 0, len(nums) - 1)
    def constructBST(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(nums[mid])

        root.left = self.constructBST(nums, start, mid - 1)
        root.right = self.constructBST(nums, mid + 1, end)

        return root