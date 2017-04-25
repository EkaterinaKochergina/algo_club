import unittest

def gauss_solve(a, y):
    n=a.width()
    x=Matrix(n)
    for pos in range(n-1):
        for victim in range (pos+1, n):
            magic = a.get(victim, pos)/a.get(pos, pos)
            y.set(victim, 0, y.get(victim, 0) - y.get(pos, 0)*magic)
            for subvictim in range(pos, n):
                a.set(victim, subvictim, a.get(victim, subvictim) - a.get(pos, subvictim)*magic)
    x.set(n-1, 0, y.get(n-1, 0)/a.get(n-1, n-1))
    for pos in range(n-2, -1, -1):
        right = y.get(pos, 0)
        for p in range(pos+1, n):
            right -= x.get(p, 0)*a.get(pos, p)
        x.set(pos, 0, right/a.get(pos, pos))
    return x
