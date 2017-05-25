#!/usr/bin/python                                                              
                                                                               
import unittest                                                                

class ComplexCartesian(object):                                                         
    def __init__(self, real, imag):                                                  
        self.real = real                                           
        self.imag = imag                                   
                     
    def __repr__(self):
        return 'ComplexCartesian({}, {})' .format(self.real, self.imag)
                                         
              
    def __add__(self, other):
        return ComplexCartesian(self.real + other.real, self.imag + other.imag)                                                   

    # def __sub__(self, other):
    #     return Complex(self.real + other.real, self.imag + other.imag)
    
    # def __div__(self, other):
    #     return Complex(self.real - other.real, self.other - self.other)

    
class ComplexPolar(object):
    pass
                                                                               
class UnittestComplex(unittest.TestCase):                                        
    def test_Complex_create(self):                                             
        num = ComplexCartesian(2.73, -12.14)                                              
        self.assertEqual(num.real, 2.73)
        self.assertEqual(num.imag, -12.14)

    def test_repr_Complex_display(self):
        num = ComplexCartesian(2.73, -12.14)  
        self.assertEqual(repr(num), 'ComplexCartesian(2.73, -12.14)')  

    def test_add_ComplexCartesian(self):
        a = ComplexCartesian(1, 3)
        b = ComplexCartesian(4, 7)
        c = a + b
        self.assertAlmostEqual(c.real, 5)
        self.assertAlmostEqual(c.imag, 10)


            
#    def test_sum_complex(self):                                               
#        self.assertEqual(a + b, Complex())                                    
                                                                               
                                                                               
if __name__=='__main__':                                                        
    unittest.main()                                                            
