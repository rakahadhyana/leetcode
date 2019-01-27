class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        i = 0
        while i < len(nums):
            if(i == 0):
                curr = nums[i]
            elif(curr == nums[i]):
                nums.pop(i)
                i -= 1
            elif(curr != nums[i]):
                curr = nums[i]
            i += 1
        return(i)

if __name__ == "__main__":
    x = Solution()
    print(x.removeDuplicates([1,2,2,3,4,5]))