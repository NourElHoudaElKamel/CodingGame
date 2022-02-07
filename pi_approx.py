from ctypes import pointer
from random import random


def piApprox():
    pts = []
    counter = 0
    nbr_pts = int((input('entrer le nombre de point?\n')))
    for i in range(0, nbr_pts):
        pt = [random(), random()]
        pts.append(pt)
    print(pts)
    for i in range(0, len(pts)):
        point = pts[i]
        x = point[0]
        print(x)
        y = point[1]
        print(y)
        if ((pow(x, 2) + pow(y, 2)) <= 1):
            counter +=1

    approximativeValueOfPi = 4 * (counter/len(pts))
    return approximativeValueOfPi
#piApprox()
print(piApprox())
