"""
The closest pair of points problem or
closest pair problem is a problem of computational geometry: given
*n* points in metric space, find a pair of points with the smallest
distance between them.
"""

# given list of tuples

from math import sqrt

def dist(p1,p2):
    """distance between two points"""

    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def bruteClosest(list_points):
    """
    Brute force solution O(n^2)
    list must be a set of points (tuples of integers)
    """

    minimum = 0
    p1 = 0
    p2 = 0
    for i in list_points:
        for k in list_points:
            
            d = dist(i,k)
            if (d < minimum and d != 0) or minimum == 0:
                p1 = i
                p2 = k
                minimum = d
    return [p1, p2, minimum]

def main():
    s = []
    r = raw_input("Points (q to quit)> ")
    while r != "q":
        s.append(eval("(" + r + ")"))
        r = raw_input("Points (q to quit)> ")

    print bruteClosest(s)

if __name__ == "__main__":

    main()