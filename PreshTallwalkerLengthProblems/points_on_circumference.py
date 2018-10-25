from Point import Point
from Circle import Circle
from random import seed

def get_rand_distance(c):
    p1 = c.random_point_on_circumference()
    p2 = c.random_point_on_circumference()
    return p1.distance_from_point(p2)

def get_avg_distance(num_samples):
    sum = 0.0
    for i in range(num_samples):
        sum += get_rand_distance(c)
    return sum / num_samples


if __name__ == "__main__":
    c = Circle(0.0, 0.0, 1.0)
    seed()

    for i in range(100000, 1000001, 100000):
        print('{0} samples, result: {1}'.format(i, get_avg_distance(i)))