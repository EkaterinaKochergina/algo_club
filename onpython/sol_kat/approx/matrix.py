import unittest
class Matrix(object):
    def __init__(self, dat):
        if type(dat)==list and type(dat[0])==list:
            self.dat=dat
        elif type(dat) == list:
            self.dat= [[t] for t in dat]

    def width(self):
                return len(self.dat[0])
 
    def height(self):
        return len(self.dat)

    def get(self, p, q):
        return self.dat[p][q]

    def __repr__(self):
        return 'Matrix(%s)'%self.dat
    
    def __mul__(self, r):
        res=Matrix(len(self.dat), len(r.dat[0]))
        for p in range(len(self.dat)):        
            for q in range(len(r.dat[0])):
                val=0
                for ind in range(len(self.dat[0])):
                    val +=self.dat[p][ind]*r.dat[ind][q]
                res.dat[p][q]=val
        return res

    def set(self, p, q, val):
        print('set: p=', p, 'q=', q, 'val=', val, 'dat=', self.dat)
        self.dat[p][q] = val
        
    def transpose(self):
        h, w=len(self.dat), len(self.dat[0])
        tm=Matrix(w, h)
        for p in range(h):
            for q in range(w):
                tm.dat[q][p]=self.dat[p][q]
        return tm

    def copy(mat):
        return[t.copy() for t in self.dat]

class TestMatrix(unittest.TestCase):
    def test_matrix_init(self):
        mat = Matrix([[11,12],[21,22],[31,32]])
        self.assertEqual(mat.height(), 3)
        self.assertEqual(mat.width(), 2)
        self.assertEqual(mat.get(2, 1), 32)
        self.assertEqual(mat.set(2, 1), 32)
        self.assertEqual(mat.transpose(), ([11, 21, 31], [12, 22, 32])

if __name__ == '__main__':
    unittest.main()
