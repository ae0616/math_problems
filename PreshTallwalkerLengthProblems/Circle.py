from random import random
from Point import Point
from math import sin, cos


class Circle:
    """ Circle class represents a circle center x,y and radius r coordinate"""

    version = '0.1'

    def __init__(self, x=0.0, y=0.0, r=1.0):
        self.origin = Point(x, y)
        self.radius = r

    def random_point_on_circumference(self):
        angle = random() * 360
        return Point(cos(angle)*self.radius+self.origin.x, sin(angle)*self.radius+self.origin.y )

    def random_point_inside(self):
        angle = random() * 360
        distance_from_origin = random() * self.radius
        return Point(cos(angle)*distance_from_origin+self.origin.x, sin(angle)*distance_from_origin+self.origin.y )

    def __repr__(self):
        return 'Circle with origin ({0},{1}) and radius {2}'.format(self.origin.x, self.origin.y, self.radius)

    def __str__(self):
        return 'Circle with origin ({0},{1}) and radius {2}'.format(self.origin.x, self.origin.y, self.radius)