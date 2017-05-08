# -*- coding:utf-8 -*-
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # def preorder(self):
    #     print(self.key)
    #     if self.leftChild:
    #         self.leftChild.preorder()
    #     if self.rightChild:
    #         self.rightChild.preorder()

'''
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
'''

r = BinaryTree('a')
r.insertLeft('b')
r.getLeftChild().insertRight('d')
print(r.getLeftChild().getRootVal())
print(r.getLeftChild().getRightChild().getRootVal())
# -----------------------------
r.insertRight('c')
r.getRightChild().insertLeft('e')
r.getRightChild().insertRight('f')
print(r.getRightChild().getRootVal())
print(r.getRightChild().getLeftChild().getRootVal())
print(r.getRightChild().getRightChild().getRootVal())


