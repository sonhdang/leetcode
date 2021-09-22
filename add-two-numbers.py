# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
def remainder_carry(num):
    remainder = num % 10
    carry = int(num / 10)
    return remainder, carry
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_sum = l1.val + l2.val
        remainder, carry = remainder_carry(next_sum)
        result_head = ListNode(remainder)
        pointer = result_head
        l1 = l1.next
        l2 = l2.next
        while(1):
            if l1 == None and l2 == None:
                if carry == 0:
                    break
                else:
                    newNode = ListNode(carry)
                    pointer.next = newNode
                    break
            else:
                if l1 != None and l2 != None:
                    next_sum = l1.val + l2.val + carry
                    l1 = l1.next
                    l2 = l2.next
                elif l1 != None and l2 == None:
                    next_sum = l1.val + carry
                    l1 = l1.next
                elif l1 == None and l2 != None:
                    next_sum = l2.val + carry
                    l2 = l2.next
                remainder, carry = remainder_carry(next_sum)
                newNode = ListNode(remainder)
                pointer.next = newNode
                pointer = pointer.next
                
        return result_head
                
                