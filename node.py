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
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, newdata):
        self.data = newdata
        
    def set_next(self, newnext):
        self.next = newnext
