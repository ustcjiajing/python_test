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
    """ reverse list """
    if head is None or head.next is None:
      return head
    p = self.reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p
  
  
if __name__ == "__main__":
    head = None
    for count in range(1, 6):
        head = Node(count, head)
    s = Solution()
    res = s.reverse_list(head)
    while res != None:
        print(res.data)
        res = res.next
