class Point:
    """ Point class represents x,y coordinate"""

    def __init__(self, x=0.0, y=0.0):
        """ create a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_point(self, p):
        return ( ((p.x - self.x)**2 + (p.y - self.y)**2)**0.5  )

    def __repr__(self):
        return 'Point at ({0},{1})'.format(self.x, self.y)

    def __str__(self):
        return 'Point at ({0},{1})'.format(self.x, self.y)
