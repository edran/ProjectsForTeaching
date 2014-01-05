"""
A happy number is defined by the following
process. Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops endlessly in a
cycle which does not include 1. Those numbers for which this process
ends in 1 are happy numbers, while those that do not end in 1 are
unhappy numbers. Display an example of your output here. Find first
8 happy numbers.
"""


def sumDigitsSquares(n):

    s = str(n)
    sum = 0
    for i in s:
        k = int(i)**2
        sum += k
    return sum


def isHappy(n):

    l = []
    while 1:
        m = sumDigitsSquares(n)
        if m == 1:
            return True
        elif m in l:
            return False
        else:
            l.append(m)
            n = m

def main():

    print __doc__
    i = 0
    n = 0
    j = int(raw_input("Numbers of happy numbers> "))
    while i < j:
        if isHappy(n):
            print n
            i += 1
        n += 1


if __name__ == "__main__":

    main()

    