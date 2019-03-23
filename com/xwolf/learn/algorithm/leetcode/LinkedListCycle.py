"""
<a href="https://leetcode.com/problems/linked-list-cycle/">141. Linked List Cycle</a>
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

@author xwolf
@status accept
@tag linkedList
"""


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListCycle:

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        res = set()
        while head is not None:
            if head in res:
                return True
            else:
                res.add(head)
            head = head.next
        return False

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


