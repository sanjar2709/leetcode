# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import Optional, List


class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            value = total % 10
            carry = total // 10

            current.next = ListNode(value)
            current = current.next

            if l2:
                l2 = l2.next
            if l1:
                l1 = l1.next

        return dummy.next


def list_to_linked_list(nums: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for num in nums:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def linked_list_to_list(node: ListNode):
    result = []
    while node:
        result.append(node.val)
        node = node.next

    return result


l1 = list_to_linked_list([2, 4, 3])
l2 = list_to_linked_list([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

result = linked_list_to_list(result)

print(result)
# from typing import Optional, List
#
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         """"""
#         dummy = ListNode()
#         current = dummy
#         carry = 0
#
#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#
#             print("--", val1, val2)
#
#             total = val1 + val2 + carry
#             carry, value = divmod(total, 10)
#
#             print("--------", total, carry, value)
#             current.next = ListNode(value)
#             current = current.next
#
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
#
#         return dummy.next
#
#
#
# def list_to_linked_list(nums: List[int]) -> Optional[ListNode]:
#     dummy = ListNode()
#     current = dummy
#
#     for num in nums:
#         current.next = ListNode(num)
#         current = current.next
#
#     return dummy.next
#
#
# l1 = list_to_linked_list([2, 4, 3])
# l2 = list_to_linked_list([5, 6, 4])
#
# data = Solution()
# result = data.addTwoNumbers(l1, l2)
# print(result)
