#!/usr/bin/env python
from IntegerQueue import *
from IntegerStack import *
from BinaryTree import *
from DictionaryGraph import *

intList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Test IntegerQueue
intQueue = IntegerQueue()
for i in intList:
    intQueue.put(i)

print "Testing IntegerQueue"
while not intQueue.empty():
    print intQueue.get()


# Test IntegerStack
stack = IntegerStack()
for i in intList:
    stack.push(i)

print "Testing IntegerStack"
while stack.checkSize() > 0:
    print stack.pop()

# Test BinaryTree
tree = BinaryTree(0)
tree.add(1, 0)
tree.add(2, 0)
tree.add(3, 1)
tree.add(4, 1)
tree.add(5, 2)
tree.add(6, 2)
tree.add(7, 3)
tree.add(8, 3)
tree.add(9, 7)

print "Testing BinaryTree with 10 integers added"
tree._print()

tree.delete(9)
tree.delete(7)

print "Testing BinaryTree with 2 integers deleted"
tree._print()

# Test graph
graph = Graph()
for i in intList:
    graph.addVertex(i)

for j in range(0, len(intList)-3):
    graph.addEdge(intList[j], intList[j+1])
    graph.addEdge(intList[j], intList[j+2])
    graph.addEdge(intList[j], intList[j+3])

print "Testing graph"
graph.findVertex(1)
graph.findVertex(3)
graph.findVertex(4)
graph.findVertex(6)
graph.findVertex(9)


