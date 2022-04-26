#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: node.py
@Author: jiajing
@Data: 2022/04/26
"""

class Node(object):
    """ 节点类 """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext
