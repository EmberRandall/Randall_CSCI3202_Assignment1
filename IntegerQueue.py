#!/usr/bin/env python
import Queue

class IntegerQueue(Queue.Queue):
    def __init__(self):
        Queue.Queue.__init__(self)
    
    # obj must be of type int
    def _put(self, obj):
        assert isinstance(obj, int), "You can't insert anything but integers into this queue"
        
        Queue.Queue._put(self, obj)

