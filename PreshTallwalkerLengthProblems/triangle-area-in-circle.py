#
# Find the average area within a triangle created with
# two points randomly selected inside a circle with radius 1
# and one point randomly selected on the circumfrence
#
from Point import Point
from Circle import Circle
from Triangle import Triangle


def get_rand_area(c):
    p1 = c.random_point_on_circumference()
    p2 = c.random_point_inside()
    p3 = c.random_point_inside()
    t = Triangle(p1, p2, p3)
    print('{0} with area {1:.2f}'.format(t, t.area()))
    return t.area()


if __name__ == "__main__":
    c = Circle(10.0, 10.0, 5.0)
    sum = 0
    samples = range(100)
    #for i in range(samples):
    #    sum += get_rand_area(c)

    avg = sum([get_rand_area(c) for ss in xrange(samples])/samples.count()
    #print('Average for {0} samples is {1:.4f}'.format(samples,sum/samples))
    print('Average for {0} samples is {1:.4f}'.format(samples.count(),avg))
