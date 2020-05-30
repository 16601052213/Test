# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/30 21:32'


# 深度优先,实际上就是二叉树或多路树先序遍历,用递归的方法
def depth_tree(tree_node):
    if tree_node is not None:
        print(tree_node._data)
        if tree_node._left is not None:
            return depth_tree(tree_node._left)
        if tree_node._right is not None:
            return depth_tree(tree_node._right)


# 广度优先,层级遍历,用队列的方法
def level_queue(root):
    if root is None:
        return
    my_queue = []
    node = root
    while my_queue:
        node = my_queue.pop(0)
        print(node.elem)
        if node.lchild is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)