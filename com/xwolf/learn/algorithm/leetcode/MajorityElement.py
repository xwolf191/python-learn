"""
169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
@author xwolf
@status accept
"""


class MajorityElement:

    def __init__(self):
        pass

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for i, v in enumerate(nums):
            if v in res.keys():
                res[v] = res[v] + 1
            else:
                res[v] = 1
        t = int(len(nums) / 2)
        for k, v in res.items():
            if v > t:
                return k


if __name__ == '__main__':
    m = MajorityElement()
    ls =  [2,2,1,1,1,2,2]
    print(m.majorityElement(ls))


