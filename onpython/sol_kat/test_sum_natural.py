import unittest

class partial_sum_natural_yield(object):
    
    def __init__(self, n):
        self.s = 0
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        for t in range(len(n)):
            self.s += self.t
        return self.s

class TestPartsum(unittest.TestCase):
    def test_partial_sum_natural(self):
        self.assertEqual(list(partial_sum_natural_yield(0, 5)), [1, 3, 6, 10, 15])

if __name__ == '__main__':
    unittest.main()
