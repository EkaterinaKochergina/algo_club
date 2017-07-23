#!/usr/bin/python

import unittest


class Stack(object):
    def __init__(self):
        self.x = [0]*10000
        self.n = 0
    
    def size(self):
        return self.n

    def push(self, a):
        self.x[self.n] = a
        self.n +=1 

    def top(self):
        return self.x[self.n - 1]

    def pop(self):
        return self.n -= 1

class TetsStack(unittest.TestCase):
    def teststack_00(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push(5)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.top(), 5)
        s.pop()
        self.assertEqual(s.size(), 0)

if __name__=='__main__':
    unittest.main()
    
