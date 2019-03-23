"""
876. Middle of the Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
Note:
The number of nodes in the given list will be between 1 and 100.

@author xwolf
@status accept
"""
import math


class MiddleOfTheLinkedList:

    def __init__(self):
        pass

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        res = []
        while head.next is not None:
            res.append(head)
            head = head.next
        n = len(res) / 2
        m = len(res) % 2
        k = 0
        if m != 0:
            k = int(math.floor(n)) + 1
        else:
            k = int(n)
        print(k)
        if len(res) == 1:
            return res[0].next
        return res[k]

    def middleNode2(self, head):
        """
        讨论区答案
        :type head: ListNode
        :rtype: ListNode
        """
        def DFS(node):
            if node:
                yield node.val
                yield from DFS(node.next)
        A = list(DFS(head))
        return A[int(len(A) / 2):]

if __name__ == '__main__':
    print(math.floor(6 / 2))
