"""A Scientific Calculator
   type h for help

   Basic symbols:
     -> x   : multiplication
     -> +   : addition
     -> -   : subtraction
     -> /   : (float) division
     -> mod : modulo
     -> sin : sine
     -> cos : cosine
     -> tan : tangent
     -> ^   : power
     -> 2^  : power of 2
"""

# This could get really fun!
# TODO Make curses interface
# TODO Check if/how to work with a stream i/o, i.e. without newline
# TODO Add floats

import math

binary = ["x",
          "+",
          "-",
          "/",
          "mod",
          "^"]

unary = ["sin",
         "cos",
         "tan",
         "2^"]

symbols = binary + unary

prompt = "Calc> "

# TODO def readPrompt(situation)

def isNumber(n):
    try:
        float(n)
        # print str(n) + " is a number!"
        return True
    except ValueError:
        return False
        
def op(symbol, x):

    if symbol in binary:
        # TODO refactor all of this with recursion over op()
        #      probably should use trees as well (boy that'd be fun)
        g = raw_input(prompt)
        if isNumber(g):
            y = eval(g) # to deal with floats
        else:
            print "Error!"
            return
            
        if symbol == "x":
            return x * y
        elif symbol == "+":
            return x + y
        elif symbol == "-":
            return x - y
        elif symbol == "/":
            return x / y
        elif symbol == "mod":
            return x % y
        elif symbol == "^":
            return pow(x, y)

    elif symbol in unary:
        if symbol == "sin":
            return math.sin(x)
        elif symbol == "cos":
            return math.cos(x)
        elif symbol == "tan":
            return math.tan(x)
        elif symbol == "2^":
            return pow(2, x)

    elif isNumber(symbol):
        return eval(symbol)

    elif symbol == "":
        return x

    else:
        print "Error"
        return x
            
def main():

    print __doc__
    while 1:
        while 1:
            g = raw_input(prompt)
            if g == "h" or g == "help":
                print __doc__
            elif isNumber(g):
                x = eval(g)
                print x
                break
            elif g == "":
                print ""
            else:
                print "Error, symbol not known. Value required."
            
        while 1:
            if x is not None:
                x = op(raw_input(prompt), x)
                print x
            else:
                break

if __name__ == "__main__":

    main()