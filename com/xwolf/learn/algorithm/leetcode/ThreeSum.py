"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

@author xwolf
@status
"""


class ThreeSum:

    def __init__(self):
        pass

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i, n in enumerate(nums):
            print(i, n)

        return res


if __name__ == '__main__':

    th = ThreeSum()
    nums = [1, 2, -2, -1, 0]
    th.threeSum(nums)


