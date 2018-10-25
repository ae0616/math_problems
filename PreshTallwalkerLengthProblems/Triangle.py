from random import random
from Point import Point


class Triangle:
    """ Triangle class represents a triangle with vertices a,b,c """

    version = '0.1'

    def __init__(self, a1: Point, a2: Point, a3: Point):
        self.a = a1
        self.b = a2
        self.c = a3

    def area(self):
        return abs((self.a.x*(self.b.y-self.c.y)+self.b.x*(self.c.y-self.a.y)+self.c.x*(self.a.y-self.b.y))/2.0)

    def __repr__(self):
        return 'Triangle ({0:.2f},{1:.2f}) ({2:.2f},{3:.2f}) ({4:.2f},{5:.2f}) '.format(
            self.a.x, self.a.y, self.b.x, self.b.y, self.c.x, self.c.y)

#    def __str__(self):
#        return 'Triangle with vertices ({0},{1}), ({2},{3}), ({4},{5}) '.format(
#            self.a.x, self.a.y, self.b.x, self.b.y, self.c.x, self.c.y)


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(0, 1)
    p3 = Point(1, 1)
    t = Triangle(p1, p2, p3)

    print('Triangle {0} has area {1:.2f}'.format(t, t.area()))

    a2 = Point(0, 2)
    a3 = Point(2, 2)
    t2 = Triangle(p1, a2, a3)
    print('Triangle {0} has area {1}'.format(t2, t2.area()))