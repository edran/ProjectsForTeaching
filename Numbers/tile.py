"""
Calculate the total cost of tile it would take to cover a floor plan
of width and height, using a cost entered by the user.
"""

import sys

def tileCost(n, w, h):
    return n * w * h


def main(argv = sys.argv):
    try:
        n = int(argv[1])
        w = int(argv[2])
        h = int(argv[3])
    except:
        n = int(raw_input("Cost per tile? "))
        w = int(raw_input("Width? "))
        h = int(raw_input("Height? "))
        
    print tileCost(n, w, h)


if __name__ == "__main__":
    # I don't think I've understood this problem...
    main()