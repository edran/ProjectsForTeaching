"""
Converts various units between one another.

    h   : help
    km  : kilometers
    m   : meters
    cm  : centimeters
    mm  : millimeters

"""

# TODO 

import math

measures = {"mm" : 0.01, "cm" : 0.1, "m" : 1, "km" : 1000}


def ConvLen(x, f, t):
    
    fm = measures[f]
    tm = measures[t]
    diff = math.ceil(math.log(fm,10)) - math.ceil(math.log(tm,10))

    return x * pow(10, diff)

def main():

    print __doc__

    x = raw_input("Starting unit> ")
    if x == "h" or x not in measures:
        return None
    y = raw_input("Ending unit> ")
    if y == "h" or y not in measures:
        return None
    n = eval(raw_input("value> "))

    print ConvLen(n, x, y)


if __name__ == "__main__":
    while 1:
        main()

