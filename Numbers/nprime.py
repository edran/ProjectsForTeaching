"""
Have the program find prime numbers until the user chooses to stop
asking for the next one.
"""

def isPrime(n):
    
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def findNextPrime(n):
    n += 1
    while 1:
        if isPrime(n):
            return n
            #break
        else:
            n += 1

def main():
    n = 0
    while 1:
        a = raw_input("Wanna find a prime number? [Yy/Nn]")
        if a in "Yy":
            n = findNextPrime(n)
            print n
        else:
            break

if __name__ == "__main__":

    main()