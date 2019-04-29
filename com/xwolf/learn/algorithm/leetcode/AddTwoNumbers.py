"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

@author xwolf
@tag
@status
"""


class ListNode:

     def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbers:

    def __init__(self):
        pass

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = []
        b= []
        while l1.next is not None:
            a.append(l1.val)
        while l2.next is not None:
            b.append(l2.val)
        print(a)
        print(b)




