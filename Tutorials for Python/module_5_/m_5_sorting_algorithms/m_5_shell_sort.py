import math


def shell_sort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return array


def shell_sort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


alist = [12, 34, 25, 15, 67, 23, 11, 86]
shell_sort(alist)
print(alist)
