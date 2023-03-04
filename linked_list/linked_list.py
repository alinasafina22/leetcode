from typing import Optional

'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        temp = head
        while temp.next:
            count += 1
            temp = temp.next
        middle = count // 2 + 1
        count = 1  
        temp = head
        while count < middle:
            count += 1
            temp = temp.next
        return temp
