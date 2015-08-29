#!/usr/bin/env python
class Graph(object):
    def __init__(self):
        self.dict = {}
    
    # add vertex to the graph
    def addVertex(self, value):
        if self.dict.has_key(value):
            print "Vertex already exists"
            return
        self.dict[value] = []
    
    # add edge between vertices value1 and value2 if both exist
    def addEdge(self, value1, value2):
        if not (self.dict.has_key(value1) and self.dict.has_key(value2)):
            print "One or more vertices not found"
            return
        self.dict[value1].append(value2)
        self.dict[value2].append(value1)
    
    # find vertex value
    def findVertex(self, value):
        if (self.dict.has_key(value)):
            print ("Adjacent vertices for key %i" % value)
            for i in self.dict[value]:
                print i
