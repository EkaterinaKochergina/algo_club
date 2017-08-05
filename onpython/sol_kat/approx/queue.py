#!/usr/bin/python


import unittest


class Queue(object):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.n = 5
        self.dat = [0]*self.n 

    def next(self, p):
        return (p+1)%self.n

    def push(self, v):
        self.dat[self.b] = v
        self.b = self.next(self.b)

    def pop(self):
        self.a = self.next(self.a)

    def size(self):
        if self.b >= self.a:
            return self.b - self.a
        return self.n - (self.a - self.b)

    def front(self):
        return self.dat[self.a]

    def last(self, p):
        return (self.n+(p-1))%self.n

    def back(self):
        return self.dat[self.last(self.b)]


class Unittest_Queue(unittest.TestCase):
    def test_queue_00(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        q.push(13)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.front(), 13)
        q.push(3)
        q.push(7)
        q.push(674)
        self.assertEqual(q.size(), 4)
        self.assertEqual(q.back(), 674)
        q.pop()
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.front(), 3)


if  __name__ == '__main__':
    unittest.main()
