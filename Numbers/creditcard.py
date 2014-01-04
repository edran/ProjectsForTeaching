"""
Takes in a credit card number from a common credit card vendor
(Visa, MasterCard, American Express, Discoverer) and validates it to
make sure that it is a valid number (look into how credit cards use
a checksum)."""

# Luhn algorithm 


def luhnSum(numbers):
    """
    Luhn Algorithm:
    From the rightmost digit, which is the check digit, moving left,
    double the value of every second digit; if product of this
    doubling operation is greater than 9 (e.g., 7 * 2 = 14), then sum
    the digits of the products (e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5).
    Take the sum of all the digits. (From Wikipedia)
    """
    l = []
    for k in range(len(numbers)): # reverse the string
        i = numbers[k]
        if k % 2 != 0:
            i *= 2
            if i > 9:
                k = str(i)
                i = int(k[0]) + int(k[1])
        l.append(i)
    check = sum(l)

    return check


def isLuhnSum(numbers):

    return (luhnSum(numbers) % 10) == 0


def isVisa(card):

    if card.startswith("4") and \
       (len(card) == 13 or len(card) == 16) and \
       isLuhnSum(card):
        return True
    else:
        return False


def isMurican(card):

    if card.startswith("34") or card.startswith("37") and \
       len(card) == 15 and \
       isLuhnSum(card):
        return True
    else:
        return False
 

def isMaster(card):
    
    if card[:2] in range(51,56) and \
       len(card) == 16 and \
       isLuhnSum(card):
        return True
    else:
        return False

        
def main():

    print __doc__
    
    s =  """
    0 - Visa
    1 - American Express
    2 - MasterCard
    """
    print s
    i = raw_input("Choose> ")
    card = raw_input("Card Number> ")
    if i == "0":
        print isVisa(card)
    elif i == "1":
        print isMurican(card)
    elif i == "2":
        print isMaster(card)
    else:
        print "Error, type of card not recognised"

if __name__ == "__main__":

    main()
    