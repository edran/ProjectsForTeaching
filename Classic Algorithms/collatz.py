"""
Start with a number *n > 1*. Find the number
of steps it takes to reach one using the following process: If *n*
is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1.
"""

def collatz(n):
    
    step = 0
    while n != 1:
        if (n % 2 == 0):
            n = n / 2
        else:
            n = n*3 + 1
        step += 1
    return step
            
        

def main():

    print __doc__
    
    n = int(raw_input("Number> "))
    if n > 1:
        print collatz(n)
    else:
        print "Invalid number"
        
if __name__ == "__main__":

    main()