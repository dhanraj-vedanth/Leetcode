from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode):
        if (head is None):
            return head
        if (head.next is None):
            return head
        prev = None
        curr = head
        while(curr is not None):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev


def generatelist(input_nodes: List):
    res = []
    for each in input_nodes:
        node = ListNode(each)
        res.append(node)
    res.append(None)
    head = res[0]
    index = 0
    while(index < len(res)-1):
        res[index].next = res[index+1]
        index += 1
    return head


head = generatelist([1, 2, 3, 4, 5])
solution = Solution()
return_head = solution.reverseList(head=head)
print("Reversed elements\n")
while (return_head is not None):
    print(f"Val -> {return_head.val}")
    return_head = return_head.next
