"""
Enter a number and have the program generate the Fibonacci sequence
to that number or to the Nth number.
"""

import sys



def fib(n):
    """
    Returns list with fibonacci numbers up till nth number.
    It assumes the sequence starts from 1
    """
    f = 0
    g = 1
    l = []
    for i in range (n):
        l.append(g) # append f if wanting to include 0 in sequence
        s = g
        g = f + g
        f = s
    
    return l


def main(argv = sys.argv):

    n = int(argv[1])
    print fib(n)

if __name__ == "__main__":

    main()
    