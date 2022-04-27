#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: deleteNode.py
@Author: jiajing
@Data: 2022/04/27
"""

#请编写一个函数，用于删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。题目数据保证需要删除的节点 不是末尾节点 。

class Solution(object):
    """
    """
    def deleteNode(self, node):
        """
        """
        node.data = node.next.data
        node.next = node.next.next
        
 
