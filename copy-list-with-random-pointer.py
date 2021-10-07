# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    # Traverse the original list using the next pointer
    #   At each node, create a new Node for the copy list
    #   Set the pointer of the previous node to point to the current node
    # WE NOW HAVE A DEEP COPY WITH ALL THE NEXT RELATIONSHIP PRESERVED
    # 
    # NOW FILL IN THE RANDOM POINTER
    # Iterate through every element of the original LinkedList (p1) and copy LinkedList (p2):
    #   If the random pointer is null
    #       assign the random pointer of the copy LinkedList to null
    #   Else:
    #       Use the random pointer to get to the random node
    #       value = value of the random node
    #       Traverse along the copy LinkedList with a while loop until null with pointer p:
    #           if p.value = value and compare(p, p1):
    #               assign p2.random = p
        
    # Function to check if two subLinkedList are the same compareLinkedList(l1,l2)
    def compareLists(l1, l2):
        while l1 != None and l2 != None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        if l1 == None and l2 == None:
            return True
        else:
            return False
        
    # CREATE COPY LIST
    if head == None:
        return None
    else:
        copy_head = Node(head.val)    
        p1 = head
        p2 = copy_head
        while (p1.next != None):
            p1 = p1.next
            p2.next = Node(p1.val)
            p2 = p2.next
        
    # FILL IN THE RANDOM POINTER
    p1 = head
    p2 = copy_head
    p_random = p1.random
    while p1 != None:   # Traverse p1 to check random pointer
        if p1.random != None:
            p_random = p1.random
            check_value = p_random.val
            p_check = copy_head
            while p_check != None:  # Traverse p_check on the Copy List
                if p_check.val == check_value and compareLists(p_check, p_random):
                    p2.random = p_check
                    break;
                p_check = p_check.next
        p1 = p1.next
        p2 = p2.next
        
    return copy_head