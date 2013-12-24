"""
Have the user enter a number and find all Prime Factors (if there
are any) and display them.
"""

import math
import sys

def isPrime(n):
    for i in range(2,int(math.sqrt(n)) + 1): # premature optimization? AH!
        if n % i == 0:
            return False

    return True


def primeFacts(n):
    l = []
    for i in range(1,int(math.ceil(n/2))+1):
        if n % i == 0 and isPrime(i):
            l.append(i)

    if n not in l and isPrime(n):
        l.append(n) # for prime numbers
    return l

def main():

    i = int(raw_input("Factors of which number? "))

    print primeFacts(i)


if __name__ == "__main__":
    while 1:
        main()
