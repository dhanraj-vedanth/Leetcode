# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> ListNode:
        """
        Not O(1) space but gets the job done well
        """
        init_set = set()
        while headA is not None:
            init_set.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in init_set:
                return headB
            headB = headB.next

        """
        Other idea is to traverse both the lists one by one at each iteration and 
        end up at the same node
        """
        tempa = headA
        tempb = headB
        a_flag = 0
        b_flag = 0
        while (tempa != tempb):
            if a_flag == 0 and tempa.next is not None:
                a_flag = 1
                tempa = headB
            else:
                tempa = tempa.next
            if b_flag == 0 and tempb.next is not None:
                b_flag = 1
                tempb = headA
            else:
                tempb = tempb.next

        return tempa
