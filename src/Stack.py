# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/6/7 15:51'


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)  # 添加元素
        self.size += 1  # 栈元素数量加 1
        return self.stack

    def pop(self):
        pop = self.stack.pop()  # 删除栈顶元素
        self.size -= 1  # 栈元素数量减 1
        return pop

    def isEmpty(self):
        return self.stack == []

    def sizes(self):
        return self.size

    def peek(self):
        return self.stack[-1]


if __name__ == "__main__":  # 这里假定 A 是 4，B 是 'dog'
    s = Stack()
    s.isEmpty()
    print(s.push(4))
    print(s.push('dog'))
    print(s.peek())
    print(s.pop())
    s.isEmpty()
