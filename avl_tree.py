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
                node.set_right(Node(value))
            else:
                self._insert_recursive(node.right, value)
        elif node.value > value:
            if node.left == None:
                node.set_left(Node(value))
            else:
                self._insert_recursive(node.left, value)

    def delete(self, value):
        if self.root.value == value:
            self.root = self._delete_recursive(self.root, value)
        else:
            successor = self._delete_recursive(self.root, value)
            print successor

    def _delete_recursive(self, root, value):
        if root is not None:
            if value < root.value:
                root.left = self._delete_recursive(root.left, value)
            elif value > root.value:
                root.right = self._delete_recursive(root.right, value)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    successor = self._search_successor(root)
                    successor.set_left(root.left)
                    successor.set_right(root.right)
                    root.parent = None
                    return successor

    def _search_successor(self, node):
        if node.right.left is None:
            successor = node.right
            node.set_right(node.right.right)
            return successor
        else:
            node = node.right
            while node.left.left is not None:
                node = node.left
            successor = node.left
            node.set_left(node.left.right)
            return successor


class AVLTree(BinaryTree):
    def __init__(self, root=None):
        super(AVLTree, self).__init__(root)



if __name__ == '__main__':
    avl_tree = AVLTree()
    values = [23, 54, 72, 76, 50, 67, 17, 19, 12, 14, 9]
    for value in values:
        avl_tree.insert(value)
        print repr(avl_tree)

    avl_tree.delete(50)
    print repr(avl_tree)

    avl_tree = AVLTree()
    values = range(13)
    for value in values:
        avl_tree.insert(value)
        print repr(avl_tree)

    avl_tree.delete(0)
    print repr(avl_tree)
    avl_tree.delete(11)
    print repr(avl_tree)
