#!/usr/bin/python

import unittest


class Car(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        self.y = self.y + 1

    def down(self):
        self.y = self.y - 1
            
    def right(self):
         self.x = self.x + 1 

    def left(self):
        self.x = self.x - 1

    def pos(self):
        return self.x, self.y

class TestCar(unittest.TestCase):
    def test_car_init(self):
        lorry = Car(7, 3)
        nissan = Car(4, 5)
        self.assertEqual(lorry.x, 7)
        self.assertEqual(nissan.x, 4)
        self.assertEqual(lorry.y, 3)
        self.assertEqual(nissan.y, 5)

    def _test_move_car(self):
        lorry = Car(3, 6)        
        lorry.up()
        lorry.down()
        lorry.right()
        lorry.left()
        self.assertEqual(lorry.up(), (3, 8))
        self.assertEqual(lorry.down(), (3, 7))
        self.assertEqual(lorry.right(), (4, 7))
        self.assertEqual(lorry.left(), (3, 7))
        self.assertEqual(lorry.pos(), (3, 7))

if __name__ == '__main__':
    unittest.main()















