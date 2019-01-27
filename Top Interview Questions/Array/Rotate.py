class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            x = nums.pop(len(nums) - 1)
            nums.insert(0, x)
        
if __name__ == "__main__":
    solution = Solution()
    solution.rotate([1,2,3,4,5,6,7], 3)