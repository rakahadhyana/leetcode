# class Solution:
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         intersect = []
#         for i in range(len(nums1)):
#             x = nums1.pop(0)
#             for j in range(len(nums2)):
#                 if(x == nums2[j]):
#                     y = nums2.pop(j)
#                     intersect.append(y)
#                     break   
#         return(intersect)

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        countNums = {}
        intersect = []
        for num in nums1:
            if num in countNums:
                countNums[num] += 1
            else:
                countNums[num] = 1
        for num in nums2:
            if num in countNums:
                if countNums[num] > 0:
                    countNums[num] -= 1
                    intersect.append(num)
        return intersect

        

if __name__ == "__main__":
    solution = Solution()
    print(solution.intersect([4,9,5], [9,4,9,8,4]))