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

    def is_left_child(self):
        return self.parent is not None and self.parent.left == self

    def is_right_child(self):
        return self.parent is not None and self.parent.right == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None

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

    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__unicode__()

class BinaryTree(Tree):
    def __init__(self, root=None):
        super(BinaryTree, self).__init__(root)

    def find(self, value):
        return _find_recursive(self.root, value)

    def _find_recursive(self, node, value):
        if node == None:
            return None
        elif value == node.value:
            return node
        elif value > node.value:
            return self._find_recursive(node.right, value)
        else:
            return self._find_recursive(node.left, value)

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value > node.value:
            if node.right == None:
                node.set_right(Node(value))
            else:
                self._insert_recursive(node.right, value)
        elif value < node.value:
            if node.left == None:
                node.set_left(Node(value))
            else:
                self._insert_recursive(node.left, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.left = self._delete_recursive(root.left, value)
        elif value > root.value:
            root.right = self._delete_recursive(root.right, value)
        else:
            if root.left is None:
                root.parent = None
                return root.right
            elif root.right is None:
                root.parent = None
                return root.left

            successor = self._search_successor(root)
            root.value = successor.value
            root.right = self._delete_recursive(root.right, successor.value)

        return root

    def _search_successor(self, node):
        return self._find_left_most(node.right)

    def _find_left_most(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


class AVLTree(BinaryTree):
    def __init__(self, root=None):
        super(AVLTree, self).__init__(root)



if __name__ == '__main__':
    avl_tree = AVLTree()
    values = [23, 54, 72, 76, 50, 67, 17, 19, 12, 14, 9]
    for value in values:
        avl_tree.insert(value)

    print "Testing deletion..."
    print repr(avl_tree)
    avl_tree.delete(54)
    print repr(avl_tree)
    avl_tree.delete(23)
    print repr(avl_tree)

    avl_tree = AVLTree()
    values = range(13)
    for value in values:
        avl_tree.insert(value)

    print "Testing deletion..."
    print avl_tree
    avl_tree.delete(0)
    print avl_tree
    avl_tree.delete(11)
    print avl_tree
