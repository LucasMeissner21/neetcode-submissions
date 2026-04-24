# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val <= list2.val:
            res = list1
            list1 = list1.next
        else:
            res = list2
            list2 = list2.next

        head = res

        while list1 or list2:
            if not list1:
                res.next = list2
                break
            elif not list2:
                res.next = list1
                break
            elif list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next

        return head