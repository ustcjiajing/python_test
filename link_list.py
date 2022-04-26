#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: link_list.py
@Author: jiajing
@Data: 2022/04/26
"""

from node import Node    

class LinkList(object):
    """ 单链表 """
    def __init__(self):
        self.head = Node   

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            count = count.getNext()
        return count
        
    def get(self, index):
        """ 取链表中第index个节点的值。如果索引无效，则返回-1 """
        if index < 0 or index >= self.length():
            return 
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next      #第一次循环后，cur为真正的头节点
        return cur.value        #循环结束后，cur为index的节点
    
    def search(self, val):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == val:
                found = True
            else:
                current = current.getNext()
        return found
        
    def addAtHead(self, val):
        """ 在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点 """
        temp = Node(val)
        temp.setNext(self.head)
        self.head = temp
        
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
    
    def remove(self, val):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == val:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
    def deleteAtIndex(self, index):
        """ 如果索引index有效，则删除链表中的第index个节点 """
        pass
       
