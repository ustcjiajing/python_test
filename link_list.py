#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: link_list.py
@Author: jiajing
@Data: 2022/04/30
"""

import node

class LinkList(object):
    """ 无序单链表 """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """链表是否为空"""
        reutrn self.head. == None

    def length(self):
        """链表长度"""
        cur = head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

    def add(self, item):
        """向链表中添加节点，头插法"""
        node = node.Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """向链表中添加节点，尾插法"""
        node = node.Node(item)
        if self.is_empty():
            self.head = None
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def insert(self, pos, item):
        """向指定位置添加节点"""
        if pos < 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.head
            count = 0
            while count < (pos -1):
                count += 1
                pre = pre.next
            node = node.Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.head
        pre = None
        while cur!= None:
            if cur.data == item:
                # 先判断此节点是否为头节点
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.head
        while cur != None:
            if cur.data == item:
                return True
            else:
                cur = cur.next
        return False    
