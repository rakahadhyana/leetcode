class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if(nums[i] == nums[i+1]):
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1,1,2,3,4]))