#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: list.py
@Author: jiajing
@Data: 2022/04/26
"""

class Node(object):
    """ 节点类 """
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkList(object):
    """ 单链表 """
    def __init__(self, Node=None):
        self._head = Node   
    
    def get(self, index):
        """ 取链表中第index个节点的值。如果索引无效，则返回-1 """
        if index < 0 or index >= self.length():
            return 
        cur = self._head
        for _ in range(index + 1):
            cur = cur.next      #第一次循环后，cur为真正的头节点
        return cur.value        #循环结束后，cur为index的节点

    def isEmpty(self):
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0
        else:
            cur = self.__head
            cnt = 1
            while cur._next != None:
                cnt += 1
                cur = cur._next
            return cnt
    
    def addAtHead(self, val):
        """ 在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点 """
        pass

    def addAtTail(self, val):
        """ 将值为 val 的节点追加到链表的最后一个元素 """
        pass
    
    def addAtIndex(self, index, val):
        """ 
        在链表中的第index个节点前添加值为val的节点。
        如果index等于链表的长度，则该节点将附加到链表的末尾。
        如果index大于链表长度，不会插入节点。
        如果index小于0，则在头部插入节点 
        """
        pass
    
    def deleteAtIndex(self, index):
        """ 如果索引index有效，则删除链表中的第index个节点 """
        pass
       
