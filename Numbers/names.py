"""
Spells negative, floating point, integer numbers.
Valid input is obviously a number
"""

digits = ["zero", "one", "two", "three", "four", "five",
          "six", "seven", "eight", "nine","ten", "eleven", "twelve",
          "thirteen", "fourteen", "fifteen", "sixteen",
          "seventeen", "eighteen", "nineteen"]

decimals = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty",
            "seventy", "eighty", "ninty"]

suffixes = ["", "", "hundred", "thousand", "million", "bilion"]

def name(n):

    s = ""
    
    # billions
    m = int(n/1000000000)
    if m != 0:
        s = s + name(m) + "-" + suffixes[5]
        if m > 1:
            s += "s"
        n -= m * 1000000000

    # millions
    m = int(n/1000000)
    if m != 0:
        if s is not "":
            s += "-"
        s = s + name(m) + "-" + suffixes[4]
        if m > 1:
            s += "s"
        n -= m * 1000000

            
    # thousands
    m = int(n/1000)
    if m != 0:
        if s is not "":
            s += "-"
        s = s + name(m) + "-" + suffixes[3]
        if m > 1:
            s += "s"
        n -= m * 1000

    
    # hundreds
    m = int(n/100)
    if m != 0:
        if s is not "":
            s += "-"
        s = s + digits[m] + "-" + suffixes[2]
        if m > 1:
            s += "s"
        n -= m * 100

    # decimals
    m = int(n)
    if m != 0:
        if s is not "":
            s += "-"
        if m < 20:
            s = s + digits[m]
        else:
            d = m/10
            u = m - d*10
            s = s + decimals[d]
            if u != 0:
                s = s + "-" + digits[u]
                
    return s


def main():

    print __doc__
    
    s = ""
    n = eval(raw_input("Number> "))

    # I have to do this because I don't want to break the
    # recursive function.
    
    if int(n) == 0:
        s = s + "zero"
    if n < 0:
        s = s + "minus "
        n = n * -1

    # integer
    s = s + name(int(n))

    # float
    r = n - int(n)
    # something weird happens here: python chances
    # the floating points somehow adding some kind of error.
    # Also, it limits the number to 12 digits
    # TODO: fix this? (but why?)
    if r != 0:
        r = int(str(r)[2:])
        s = s + " point " + name(r)

    # finally
    print s


if __name__ == "__main__":

    main()
