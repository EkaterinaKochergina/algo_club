#!/usr/bin/python                                                              
                                                                               
import unittest                                                                

class Complex(object):                                                         
    def __init__(self, a, b):                                                  
        self.a = a                                           
        self.b = b                                   
                                                                               
#    def __add__(self, obj):                                                   
                                                                               
                                                                               
class UnittestComplex(unittest.TestCase):                                        
    def test_Complex_create(self):                                             
        a = Complex(2,3)                                                      
        b = Complex(-4,1)                                                      
                                                                               
#    def test_sum_complex(self):                                               
#        self.assertEqual(a + b, Complex())                                    
                                                                               
                                                                               
if __name__=='__main__':                                                        
    unittest.main()                                                            
