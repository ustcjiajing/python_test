# leetcode 2: 两数相加
"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        pre = cur = ListNode()
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            result = x + y + carry
            cur.next = ListNode(result % 10)
            cur = cur.next
            carry = result // 10

            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        if carry: 
            cur.next = ListNode(carry)

        return pre.next 

# 时间复杂度：O(max(m,n))，其中 m 和 n 分别为两个链表的长度。我们要遍历两个链表的全部位置，而处理每个位置只需要 O(1) 的时间。
# 空间复杂度：O(1)。注意返回值不计入空间复杂度。
