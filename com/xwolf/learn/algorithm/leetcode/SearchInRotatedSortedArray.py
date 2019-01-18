
"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

@author xwolf
@status
"""
class SearchInRotatedSortedArray:

    def __init__(self):
        pass

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        idx = nums.index(target)
        t = 0
        if idx == 0 :
            t = 1
        else:
            t = idx
        a = nums[0:t]
        b = nums[t:]
        print(a)
        print(b)
        if sorted(b) == b and sorted(a) == a:
            return idx
        return -1


if __name__ == '__main__':
    sr = SearchInRotatedSortedArray()
    nums = [3 , 5, 1 ]
    target = 1
    result = sr.search(nums,target)
    print(result)
