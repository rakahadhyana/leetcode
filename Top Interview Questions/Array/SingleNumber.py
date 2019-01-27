class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums): 
            if i == len(nums) - 1:
                return nums[i]
            elif nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([4,1,2,1,2]))
    print(solution.singleNumber([2,2,1]))
