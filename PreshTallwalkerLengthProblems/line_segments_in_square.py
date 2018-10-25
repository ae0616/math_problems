from Point import Point
from random import random
from datetime import datetime


def random_length():
    t1 = Point(random(), random())
    t2 = Point(random(), random())
    return t1.distance_from_point(t2)

def avg_length(iterations):
    t = 0.0
    for i in range(iterations):
        t += random_length()
    return t / iterations



if __name__ == "__main__":
    from random import seed


    seed()
    iterations = 10000000
    answer = avg_length(iterations)
    print('Answer = {0} based on {1} random line segments'.format(answer, iterations))
