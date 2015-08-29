#!/usr/bin/env python

class IntegerStack(object):
    def __init__(self):
        self.stack = []
    
    # obj must be of type int
    def push(self, obj):
        assert isinstance(obj, int), "You can't insert anything but integers into this stack"
        
        self.stack.append(obj)
    
    # remove the last item from the stack and return it
    def pop(self):
        return self.stack.pop()
    
    # return the size of the stack
    def checkSize(self):
        return len(self.stack)