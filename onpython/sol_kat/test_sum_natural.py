import unittest

class Box2(object):
    def __init__(self):
        self.s = 0
        self.t = 1
        
    def __next__(self):
        self.s += self.t
        self.t += 1
        if self.t > n:
            raise StopIteration()
        return self.s
    
    def __iter__(self):
        return self


class TestPartsum(unittest.Test.Case):
    def test_partial_sum_natural(self):
        self.assertUqual(list(partial_sum_natural_yield(5)), [1, 3, 6, 10, 15])
