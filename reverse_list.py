#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: reverse_list.py
@Author: jiajing
@Data: 2022/04/26
"""

from node import Node

class Solution(object):
  """
  """
  def reverse_list(self, head):
    """ 反转链表：递归法 """
    if head is None or head.next is None:
        return head
    p = self.reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p
  
   def reverse_list(self, head):
     """ 反转链表：迭代法 """
     if head is None or head.next is None:
         return head
     pre, cur = None, head
     while cur is not None:
         next = cur.next
         cur.next = pre
         pre = cur
         cur = next
     return pre
  
if __name__ == "__main__":
    head = None
    for count in range(1, 6):
        head = Node(count, head)
    cur = head
    while cur is not None:
        print(cur.data)
        cur = cur.next
    
    s = Solution()
    res = s.reverse_list(head)
    
    print("===================")
    while res is not None:
        print(res.data)
        res = res.next
