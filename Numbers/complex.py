"""
Show addition, multiplication, negation,
and inversion of complex numbers in separate functions. (Subtraction
and division operations can be made with pairs of these operations.)
Print the results for each operation tested.
"""

from math import sqrt

from copy import copy

class Complex(object):

    def __init__(self, real, immaginary):
        self.imm = immaginary
        self.real = real

    def __str__(self):
        if self.imm >= 0:
            return str(self.real) + "+" + str(self.imm) + "i"
        else:
            return str(self.real) + str(self.imm) + "i"

    def add(self, comp):
        self.real += comp.real
        self.imm += comp.imm

    def subtract(self, comp):
        self.real -= comp.real
        self.imm -= comp.imm

    def multiply(self, comp):
        self.real = self.real * comp.real - (self.imm * comp.imm)
        self.imm = (self.real * comp.imm) + (self.imm * comp.real)

    def divide(self, comp):
        
        a = self.real
        b = self.imm
        c = comp.real
        d = comp.imm

        divisor = sqrt(c) + sqrt(d)
        if divisor != 0:
            self.real = (a*c + b*d) / divisor
            self.imm = (b*c - a*d) / divisor
        else:
            print "Divisor can't be 0"

            
def cSum(c1, c2):
    r = copy(c1)
    r.add(c2)
    return r

def cSubtraction(c1, c2):
    r = copy(c1)
    r.subtract(c2)
    return r

def cMultiplication(c1, c2):
    r = copy(c1)
    r.multiply(c2)
    return r

def cDivision(c1, c2):
    r = copy(c1)
    r.divide(c2)
    return r

def main():

    print __doc__


    


if __name__ == "__main__":

    main()