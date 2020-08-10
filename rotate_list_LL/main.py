# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        fake_head = head
        for n in range(k):
            t = head
            t2 = head
            t2 = t2.next
            while(t2):
                # print(t.val)
                # print(t2.val)
                if t2.next == None:
                    # print("ulla vanten aathaaaaa")
                    t.next = t.next.next
                    t2.next = head
                    head = t2
                    break

                else:
                    t2 = t2.next
                    t = t.next 
                    # print(t.val)
                    # print(t2.val)
        return t2


t1 = ListNode(1)
t2 = ListNode(2)
t3 = ListNode(9)
t1.next = t2
t2.next = t3

l1 = t1


s = Solution()
ans = s.rotateRight(l1,2)

while(ans):
    print(ans.val)
    ans = ans.next