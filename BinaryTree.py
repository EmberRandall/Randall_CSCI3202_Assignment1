#!/usr/bin/env python
class BinaryTree(object):
    def __init__(self, rootKey):
        self.rootNode = TreeNode(rootKey)
    
    # walk through tree to find node containing value
    def findNode(self, parentNode, value):
        if parentNode.getKey() == value:
            return parentNode
        
        if parentNode.getLeftChild() != None:
            node = self.findNode(parentNode.getLeftChild(), value)
            if node != None:
                return node
        
        if parentNode.getRightChild() != None:
            node = self.findNode(parentNode.getRightChild(), value)
            if node != None:
                return node
        
        return None
    
    # add node containing value as a child to node containing parentValue
    def add(self, value, parentValue):
        node = TreeNode(value)
        parent = self.findNode(self.rootNode, parentValue)
        if parent == None:
            print "Parent not found"
            return
        
        if parent.getLeftChild() == None:
            parent.setLeftChild(node)
        elif parent.getRightChild() == None:
            parent.setRightChild(node)
        else:
            print "Parent has two children, node not added"
    
    # delete node containing value if it is childless
    def delete(self, value):
        node = self.findNode(self.rootNode, value)
        if node == None:
            print "Node not found"
            return
        
        if node.getLeftChild() != None:
            print "Node not deleted, has children"
            return
        
        parentNode = node.getParent()
        if parentNode.getLeftChild() == node:
            parentNode.deleteLeftChild()
        elif parentNode.getRightChild() == node:
            parentNode.deleteRightChild()
    
    # print the entire tree
    def _print(self):
        self.printTree(self.rootNode)
    
    # print a subtree of the tree
    def printTree(self, node):
        if node != None:
            print node.getKey()
            self.printTree(node.getLeftChild())
            self.printTree(node.getRightChild())

# class to describe nodes of the tree
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None
    
    def getKey(self):
        return self.key
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def getParent(self):
        return self.parent
    
    def setParent(self, parentNode):
        self.parent = parentNode
    
    def setLeftChild(self, leftChild):
        self.leftChild = leftChild
        leftChild.setParent(self)
    
    def setRightChild(self, rightChild):
        self.rightChild = rightChild
        rightChild.setParent(self)
    
    def deleteLeftChild(self):
        self.leftChild = None
    
    def deleteRightChild(self):
        self.rightChild = None