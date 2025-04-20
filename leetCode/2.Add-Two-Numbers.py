# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        for i in range(max(len(l1),len(l2))): # hago un loop del maximo de los dos arrays
            if i >= len(l1):
                l1.append(0)
            if i >= len(l2):
                l2.append(0)

            # si la suma de L1[i] + L2[i] es mayor a 9, entonces guardo el carry y lo sumo al siguiente elemento
            if l1[i] + l2[i] > 9:
                
                l1[i+1] += 1
                l1[i] = (l1[i] + l2[i]) % 10
            else:
                l3[i] = l1[i] + l2[i]
            
    
        
          
        return 
        
#l1 = [2,4,3]
#l2 = [5,6,4]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

Solution().addTwoNumbers(l1, l2)

         