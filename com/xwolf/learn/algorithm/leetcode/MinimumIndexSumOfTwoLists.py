# encoding: utf-8
"""
<a href="https://leetcode.com/problems/minimum-index-sum-of-two-lists/">599. Minimum Index Sum of Two Lists</a>
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.

@author xwolf
@status accept
"""


class MinimumIndexSumOfTwoLists(object):

    def __init__(self):
        pass

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = {}
        for i in range(len(list1)):
            a = list1[i]
            if a in list2:
                j = list2.index(a)
                res[a] = i + j
        keys = sorted(res.values(),reverse=False)
        target = keys[0]
        result = []
        for key in res:
            val = res[key]
            if val == target:
               result.append(key)
        return result


if __name__ == '__main__':

     a = ["Shogun", "Tapioca Express", "Burger King", "KFC","Piatti"]
     b = ["Piatti", "The Grill at Torrey Pines","Tapioca Express", "Shogun", "Shogun"]
     min = MinimumIndexSumOfTwoLists()
     min.findRestaurant(a,b)




