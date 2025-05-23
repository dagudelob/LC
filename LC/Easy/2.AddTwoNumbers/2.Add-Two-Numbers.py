# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) ->ListNode:
        dummy = ListNode()  # Initialize dummy head
        cur = dummy         # Initialize current
        carry = 0           # Initialize carry

        while l1 or l2 or carry:
            v1 =l1.val if l1 else 0
            v2 =l2.val if l2 else 0
            
            #new digits
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            #update ptrs
            cur = cur.next  
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

# Create a linked list from a list of values
# This function is used to create a linked list from a list of values
# and is not part of the original problem statement.
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test
l1 = createLinkedList([9,9,9,9,9,9,9])
l2 = createLinkedList([9,9,9,9])
result = Solution().addTwoNumbers(l1, l2)
print("Resultado: ", end="")
while result:
    print(result.val, end=" ")
    result = result.next
