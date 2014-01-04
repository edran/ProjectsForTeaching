"""
The Factorial of a positive integer, n, is defined as the product
of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is
defined as being 1. Solve this using both loops and recursion.
"""

def recFactorial(n):

    if n >= 0:
        if n == 0:
            return 1

        return n * recFactorial(n-1)
    else:
        print "Factorial not defined for n < 0"

        
def factorial(n):

    if n >= 0:
        if n == 0:
            return 1
        else:
            sum = 1
            for i in range(1, n + 1):
                sum *= i
            return sum
    else:
        print "Factorial not defined for n < 0"


def main():

    print __doc__

    n = raw_input("Factorial of> ")
    print "Rec = %i" % recFactorial(int(n))
    print "Std = %i" % factorial(int(n))


if __name__ == "__main__":

    main()