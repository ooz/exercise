#!/usr/bin/python
# coding: utf-8
'''
File: avl_tree.py
Author: Oliver Zscheyge
Description:
    Binary and AVL tree exercise.
'''

class Node(object):
    def __init__(self, value, left=None, right=None, parent=None):
        super(Node, self).__init__()
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def set_left(self, node):
        if self.left is not None:
            self.left.parent = None
        self.left = node
        if node is not None:
            node.parent = self

    def set_right(self, node):
        if self.right is not None:
            self.right.parent = None
        self.right = node
        if node is not None:
            node.parent = self

    def __repr__(self):
        left_str = u""
        if self.left != None:
            left_str = repr(self.left)
        right_str = u""
        if self.right != None:
            right_str = repr(self.right)
        return u"(%s%s%s)" % (left_str, repr(self.value), right_str)

    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__unicode__()

class Tree(object):
    def __init__(self, root=None):
        super(Tree, self).__init__()
        self.root = root

    def find(self, value):
        raise NotImplementedError()

    def insert(self, value):
        raise NotImplementedError()

    def delete(self, value):
        raise NotImplementedError()

    def __repr__(self):
        return repr(self.root)

class BinaryTree(Tree):
    def __init__(self, root=None):
        super(BinaryTree, self).__init__(root)

    def find(self, value):
        return _find_recursive(self.root, value)

    def _find_recursive(self, node, value):
        if node == None:
            return None
        elif node.value == value:
            return node
        elif node.value < value:
            return self._find_recursive(node.right, value)
        else:
            return self._find_recursive(node.left, value)

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node.value < value:
            if node.right == None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
        elif node.value > value:
            if node.left == None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)

class AVLTree(BinaryTree):
    def __init__(self, root=None):
        super(AVLTree, self).__init__(root)




def main():
    avl_tree = AVLTree()
    values = [23, 54, 72, 76, 50, 67, 17, 19, 12, 14, 9]
    for value in values:
        avl_tree.insert(value)
    print repr(avl_tree)

if __name__ == '__main__':
    main()

