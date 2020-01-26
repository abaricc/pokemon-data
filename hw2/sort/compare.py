import random
import time
import sys
import itertools
import create
import sort

def compareSorts(myList, n):

    #Bubble sort
    sortList = myList.copy()
    start = time.time()
    sort.bubbleSort(sortList)
    end = time.time()
    print ("Bubble sort: " + str(n) + " ints in " + str(end - start))
    #print(sortList)

    #Selection sort
    sortList = myList.copy()
    start = time.time()
    sort.selectionSort(sortList)
    end = time.time()
    print ("Selection sort: " + str(n) + " ints in " + str(end - start))
    #print(sortList)

    #Insertion sort
    sortList = myList.copy()
    start = time.time()
    sort.insertionSort(sortList)
    end = time.time()
    print ("Insertion sort: " + str(n) + " ints in " + str(end - start))
    #print(sortList)

    #Merge sort
    sortList = myList.copy()
    start = time.time()
    sort.mergeSort(sortList)
    end = time.time()
    print ("Merge sort: " + str(n) + " ints in " + str(end - start))
    #print(sortList)

    #Heap sort
    sortList = myList.copy()
    start = time.time()
    sort.heapSort(sortList)
    end = time.time()
    print ("Heap sort: " + str(n) + " ints in " + str(end - start))
    #print(sortList)

    #Quick sort
    sortList = myList.copy()
    start = time.time()
    sort.quickSort(sortList, 0, len(sortList)-1)
    end = time.time()
    print ("Quick sort: " + str(n) + " ints in " + str(end - start))
    #print(sortList)

    #Radix sort
    sortList = myList.copy()
    start = time.time()
    sort.radixSort(sortList)
    end = time.time()
    print ("Radix sort: " + str(n) + " ints in " + str(end - start))
    #print(sortList)

    #Count sort
    sortList = myList.copy()
    k = max(myList)+1
    start = time.time()
    sort.countSort(sortList, k)
    end = time.time()
    print ("Count sort: " + str(n) + " ints in " + str(end - start))
    #print(sortList)

if __name__=="__main__":
    n = 10
    myList = create.createRandomIntList(n)
    compareSorts(myList, n)