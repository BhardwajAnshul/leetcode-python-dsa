

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Definition for singly-linked list.
    def list_to_linked_list(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        current = head

        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next

        return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 0

        curr = l1.val
        lx = []
        while True:
            lx.append(l1.val)
            l1 = l1.next
            if not l1:
                break
    
            

        ly = []
        while True:
            ly.append(l2.val)
            l2 = l2.next
            if not l2:
                break

        lxr = lx[::-1]
        lyr = ly[::-1]

        lxr = int("".join([str(a) for a in lxr]))
        lyr = int("".join([str(y) for y in lyr]))

        sumxy = lxr + lyr

        f =[]

        while(sumxy):
            f.append(sumxy%10)
            sumxy = sumxy//10

        print(f)


    

        if not f:
            return ListNode(val=0)

        fr = ListNode(val=f[0])

        curr = fr

        for x in f[1:]:
            curr.next = ListNode(val=x)
            # curr.val = x
            curr = curr.next

        return fr





        