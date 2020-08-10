# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
c = 0
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        global c
        return_head = head
        prev = ListNode(0)
        prev.next = return_head
        c = 0
        print(n)
        while(head):
            temp = head
            while(c != n):
                print("UP TOP")
                temp = temp.next
                if temp:
                    c += 1
                    print(temp.val,c)
                    # input()
                else:
                    c += 1
                    print("NONE DA")
                    break
            # if temp == None:
            #     if n == 1:
            #         print("INGA DA baade")
            #         prev = head
            #         prev = prev.next
            #         return prev
            #     else:
            #         prev.next = prev.next.next
            #         return return_head
            if temp == None:
                # fake_head = return_head
                # c = 0
                # while(c !=n):
                #     if fake_head == None:
                #         break
                #     else:
                #         c += 1
                #         fake_head = fake_head.next
                # if c == n:
                # if return_head.next == None:
                #     prev = head
                #     prev = prev.next
                #     return prev
                # else:
                #     prev.next = prev.next.next
                #     head1 = prev.next
                #     return head1
                prev.next = prev.next.next
                head1 = prev.next
                return head1
            else:
                print("Down here")
                c = 0
                prev = head
                head = head.next
                print(prev.val)
                print(head.val)
            
t1 = ListNode(1)
t2 = ListNode(2)
# t3 = ListNode(9)
t1.next = t2
# t2.next = t3

l1 = t1


s = Solution()
ans = s.removeNthFromEnd(l1,2)

while(ans):
    print(ans.val)
    ans = ans.next