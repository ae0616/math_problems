from random import random

def walk():
    caught = False
    door = 4
    turn = 0
    while not caught:
        if (random()<0.5):
            door -= 1
        else:
            door += 1
        if (door==1 or door==7):
            caught = True
        turn += 1
    return turn

def avg_walk(iterations):
    sum = 0
    for i in range(iterations):
        sum += walk()
    return sum / iterations

if __name__ == "__main__":
    for i in range(1000000, 10000001, 1000000):
        print('{0} samples, result: {1}'.format(i, avg_walk(i)))