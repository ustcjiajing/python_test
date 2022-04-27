#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: linke_has_cycle.py
@Author: jiajing
@Data: 2022/04/27
"""

#给你一个链表的头节点 head ，判断链表中是否有环。
#如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#如果链表中存在环 ，则返回 true 。 否则，返回 false 。

class Solution(object):
  """
  """
  def hasCycle(self, head):
      """ 哈希表 """
      if head is None or head.next is None:
          return False
      seen = set()
      while head:
          if head in seen:
              return True
          seen.add(head)
          head = head.next
      return False
    
