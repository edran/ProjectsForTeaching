"""
Implement two types of sorting algorithms: Merge sort
and bubble sort.
"""


def mergeMS(left, right):
    """
    Merge two sorted lists in a sorted list
    """
    
    llen = len(left)
    rlen = len(right)
    sumlist = []
    
    while left != [] and right != []:
        lstack = left[0]

        while right != []:
            rstack = right[0]

            if lstack < rstack:
                sumlist.append(lstack)
                left.pop(0)
                break

            else:
                sumlist.append(rstack)
                right.pop(0)

    if left == []:
        sumlist += right

    else:
        sumlist += left

    return sumlist


def mergeSort(l):
    """ 
    Divide the unsorted list into n sublists, each containing 1
    element (a list of 1 element is considered sorted).  Repeatedly
    merge sublists to produce new sorted sublists until there is only
    1 sublist remaining. This will be the sorted list.
    """

    # I actually implemented without reading any of the formal algorithms,
    # so I'm not entirely sure I did a good job. I have to read up and compare
    # my solution with a standard one.

    if len(l) == 1:
        return l
    split = len(l) / 2
    
    a = mergeMS(mergeSort(l[:split]), mergeSort(l[split:]))

    return a
    

def bubbleSort(l):
    """
    simple sorting algorithm that works by repeatedly stepping through
    the list to be sorted, comparing each pair of adjacent items and
    swapping them if they are in the wrong order
    """

    n = list(l)
    
    swapped = True
    k = len(n) - 1
    while swapped:
        swapped = False
        i = k
        while i > 0:
            u = n[i]
            d = n[i - 1]
            if u < d:
                n[i] = d
                n[i -1] = u
                swapped = True
            i -= 1

    return n


def main():

    t = raw_input("List of numbers> ")
    t = eval("[" + t + "]")
    r = mergeSort(t)
    b = bubbleSort(t)
    
    print "MergeSort: ", r
    print "BubbleSort: ", b

if __name__ == "__main__":

    main()
