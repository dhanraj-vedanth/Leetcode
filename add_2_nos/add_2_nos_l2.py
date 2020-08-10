head1 = 0
head2 = 0
headr = 0
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def carry_fn(self, result):
        # print("INHEREEEEE")
        global add_flag
        carryover = (result//10)
        result = result % 10
        # print("DOWN HEREEEE")
        return (carryover, result)

    def addTwoNumbers(self, head1: ListNode, head2: ListNode) -> ListNode:
        global add_flag
        iterator = 0
        head_check = 0
        counter_checker = 0
        carryover = 0
        while (head1) or (head2):
            result_node = ListNode(0)
            temp1 = 0
            temp2 = 0
            result = 0
            try:
                temp1 = int(head1.val)
            except:
                temp1 = 0
            try:
                temp2 = int(head2.val)
            except:
                temp2 = 0
            print(temp1,temp2)
            # input()
            result = temp1 + temp2 + carryover
            
            if result < 10:
                carryover = 0
                print("OTHA")

            else:
                while result >= 10:
                    carryover,result = self.carry_fn(result) 
                    print("KKODAAD")
            if counter_checker == 0:
                head_check = result_node
                iterator = result_node
                counter_checker = 1
            result_node.val = result
            iterator.next = result_node
            iterator = result_node

            if head1 == None and head2 != None:
                head2 = head2.next
            if head2 == None and head1!= None:
                head1 = head1.next
            else:
                head1 = head1.next
                head2 = head2.next
                print("***************")
            if head1 == None and head2 == None:
                if carryover == 1:
                    print("In here bitchass")
                    final_result = ListNode(1)
                    iterator.next = final_result
                    iterator = final_result
            print(result)
            print(carryover)
            input()
        
        print("OUT OF TTHE WILD WHILE")
        
        t_head = head_check
        while(t_head):
            print(t_head.val)
            # input()
            # print(t_head.next)
            t_head = t_head.next
            

        return head_check

    
        

t1 = ListNode(0)
# t2 = ListNode(4)
# t3 = ListNode(9)
# t1.next = t2
# t2.next = t3

t4 = ListNode(0)
# t5 = ListNode(6)
# t6 = ListNode(9)
# t4.next = t5
# t5.next = t6

l1 = t1
l2 = t4

s = Solution()
s.addTwoNumbers(l1,l2)
