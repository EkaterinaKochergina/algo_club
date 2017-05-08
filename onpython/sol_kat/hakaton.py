import unittest
        
import unittest
def shaiba(x, y, dx, dy):
    if x+dx < 100 and y+dy < 100:
        x=x+dx
        y=y+dy
    if x+dx > 100 and y+dy < 100:
        x = x + (-dx)
        y = y + dy 
    if x+dx < 100 and y+dy > 100:
        x = x+dx
        y = y+(-dy)
    if x+dx > 100 and y+dy > 100: 
        x = x+(-dx)
        y = y+(-dy)
    return x, y, dx, dy

class TestShaiba(unittest.TestCase):
    def test_next_shaiba_calculated_plus_speed(self): 
        self.assertEqual(list(shaiba(81, 20, 5, 3)), [86, 23, 5, 3])
        self.assertEqual(list(shaiba(73, 94, 5, 10)), [78, 84, 5, 10])
        self.assertEqual(list(shaiba(91, 26, 15, 32)), [76, 58, 15, 32])
        self.assertEqual(list(shaiba(96, 87, 13, 25)), [83, 62, 13, 25])


if __name__ == '__main__':
    unittest.main()

