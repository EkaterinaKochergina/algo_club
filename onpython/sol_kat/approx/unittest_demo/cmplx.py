#!/Usr/bin/python                                                              
                                                                               
import unittest                                                                
import math

class ComplexCartesian(object):                                                         
    def __init__(self, real, imag):                                                  
        self.real = real                                           
        self.imag = imag                                   
                     
    def __repr__(self):
        return 'ComplexCartesian({}, {})' .format(self.real, self.imag)
                                         
              
    def __add__(self, other):
        return ComplexCartesian(self.real + other.real, self.imag + other.imag)                                                   

    def __sub__(self, other):
         return ComplexCartesian(self.real - other.real, self.imag - other.imag)
    
    def __div__(self, other):
         return ComplexCartesian((self.real * -other.real, self.imag * -other.imag)/(other.real*-other.real), (other.imag*-other.imag))

    def __prod__(self, other):
        return ComplexCartesian(self.real*other.real, self.imag*other.imag)

    
class ComplexPolar(object):
    def __init__(self, rho, phi):
        self.rho = rho
        self.phi = phi

    def __repr__(self):
        return 'ComplexPolar({}, {})' .format(self.rho, self.phi)

    def __mul__(self, other):
         return ComplexPolar(self.rho*other.rho, self.phi + other.phi)

    def __div__(self, other):
        return ComplexPolar(self.rho/other.rho, self.phi - other.phi)

class UnittestComplexPolar(unittest.TestCase):
    def test_ComplexPolar_create(self):
        num = ComplexPolar(10, 0)
        self.assertEqual(num.rho, 10)
        self.assertEqual(num.phi, 0)

    def test_repr_Complex_display(self):
        num = ComplexPolar(10, 90)
        self.assertEqual(repr(num), 'ComplexPolar(10, 90)')

    def test_mul_ComplexPolar(self):
        a = ComplexPolar(10, 90)
        b = ComplexPolar(5, 90)
        c = a * b
        self.assertAlmostEqual(c.rho, 50)
        self.assertAlmostEqual(c.phi, 180)
        
    def test_div_ComplexPolar(self):
        a = ComplexPolar(10, 90)
        b = ComplexPolar(15, 90)
        c = a / b
        self.assertAlmostEqual(c.rho, 10/15)
        self.assertAlmostEqual(c.phi, 0)

                                                                               
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
    
    def test_sub_ComplexCartesian(self):
        a = ComplexCartesian(1, 3)
        b = ComplexCartesian(4, 7)
        c = a - b
        self.assertAlmostEqual(c.real, -3)
        self.assertAlmostEqual(c.imag, -4)
            
#    def test_sum_complex(self):                                               
#        self.assertEqual(a + b, Complex())                                    
                                                                               
                                                                               
if __name__=='__main__':                                                        
    unittest.main()                                                            
