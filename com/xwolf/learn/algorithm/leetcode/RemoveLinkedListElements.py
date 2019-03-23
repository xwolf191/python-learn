"""
203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

@author xwolf
@status accept
"""


class RemoveLinkedListElements:

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head

    def removeElements2(self, head, val):
        """
        评论区另外一个答案
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        prev = None
        cur = head
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
            else:
                prev = cur
            cur = cur.next
        return head





