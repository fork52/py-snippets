# Reference: https://binarysearch.com/problems/Circular-Queue

class CircularQueue:
    def __init__(self, capacity):
        self.f = self.r = -1
        self.q = [0] * capacity
        self.n = capacity

    def enqueue(self, val):
        if self.isFull():
            return False
        self.r = (self.r + 1) % self.n

        if self.isEmpty():
            self.f = self.r

        self.q[self.r] = val
        return True

    def dequeue(self):
        if self.isEmpty():
            return False
        
        if self.f == self.r:
            self.r = self.f = -1
        else:
            self.f = (self.f + 1) % self.n
        return True

    def front(self):
        if self.isEmpty():
            return -1
        return self.q[self.f]

    def top(self):
        if self.isEmpty():
            return -1
        return self.q[self.r]
        

    def isFull(self):
        rnext = (self.r + 1) % self.n
        return rnext == self.f

    def isEmpty(self):
        return self.f == -1
        