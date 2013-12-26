"""
Develop a converter to convert a decimal number to binary or a
  binary number to its decimal equivalent.
"""

import sys

def bToD(s):

    if not s.startswith("0b"):
        print "Only binary numbers with a 0b at the start are accepted"
        return 0 - 1 # Oh dear Cl... 

    else:
        ls = len(s) - 2
        n = 0
        for b in s[2:]: # taken 0b away
            
            n += pow(2, ls - 1) * int(b)
            ls -= 1
        return n

def dToB(i):
    """
    Decimal to Binary
    """

    s = ""
    if i == 0:
        return 0
    else:
        while i != 0:
            s += str(i % 2)
            i = i / 2
    return "0b" + s[::-1] # Reversed
    

def main():

    b1 = "0b1011"    
    b2 = "0b1111111"
    b3 = "0b101100"
    # This test won't work if there are
    # numbers that start with 0 for obvious reasons
    print dToB(bToD(b1)) == b1 
    print dToB(bToD(b2)) == b2 
    print dToB(bToD(b3)) == b3 


if __name__ == "__main__":

    main()