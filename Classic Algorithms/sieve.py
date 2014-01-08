"""
The sieve of Eratosthenes is one of the most efficient ways to find
all of the smaller primes (below 10 million or so).
"""

from math import sqrt

def sieve(n):

    p = 2
    l = range(2, n + 1) # optimized
    for i in range(2,int(sqrt(n)) + 2):
        if i in l:
            k = i + i
            while k <= n:
                if k in l:
                    l.pop(l.index(k))
                k += i
    return l

def main():

    i = int(raw_input("Max number to check> "))

    print sieve(i)


if __name__ == "__main__":

    main()