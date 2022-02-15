# -*- coding: utf-8 -*-
"""
    @Author: 49173
    date: 2022-02-08
"""


# 栈与队列
class Repeat:
    def __init__(self):
        self.__data = []

    def is_empty(self):
        """判断是否为空"""
        return self.__data == []

    def push(self, data):
        """头部添加元素"""
        self.__data.insert(0, data)

    def travel(self):
        """遍历所有元素"""
        for i in self.__data:
            print(i)
        print('')

    def find(self, v):
        """查找元素"""
        for i in self.__data:
            if v == i:
                return True
        return False

    def size(self):
        """返回队列的元素个数"""
        return len(self.__data)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, n):
        self.__data = n


class Stack(Repeat):
    def pop(self):
        """弹出顶部元素"""
        return self.data.pop(0)

    def peek(self):
        """返回栈顶元素"""
        # 先判断是否为空
        if self.is_empty():
            return False
        else:
            return self.data[0]


class Queue(Repeat):
    def pop(self):
        """队尾元素出队"""
        return self.data.pop()
