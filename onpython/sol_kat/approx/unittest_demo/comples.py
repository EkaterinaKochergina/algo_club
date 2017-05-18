#!/usr/bin/python

import unittest

class Cmplx(object):
    def __init__(self, frstnum, secnum):
        self.cmplnum = loat(frstnum)+float(secnum)*i

    def __add__(self, other): 
        res_sum_cmplx = self.cmplnum+other.cmplnum 

class UnittestComplex(unittest.TestCase):
    def test_сomplex_create(self):
        a = Cmplx(2, 3)

    def test_sum_complex(self):
        a = Cmplx(3, -4)
        b = Cmplx(1, 2)
        self.assertEqual(a + b, Cmplx(4, -2))
    

if __name__='__main__':
    unittest.main()
    
