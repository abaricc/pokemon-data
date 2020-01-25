#Reference: https://www.geeksforgeeks.org/sorting-algorithms/

#Bubble sort
def bubbleSort(arr):
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j] 

#Selection sort
def selectionSort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

#Insertion sort
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key

#Merge sort
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest) 
  
#Heap sort
def heapSort(arr): 
    n = len(arr) 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def partition(arr,low,high): 
    i = ( low-1 )
    pivot = arr[high]
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
#Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

#Count Sorts
def countingSort(arr, exp1): 
    n = len(arr)
    output = [0] * (n) 
    count = [0] * (10) 
    for i in range(0, n): 
        index = int(arr[i]/exp1) 
        count[ index % 10 ] += 1
    for i in range(1,10): 
        count[i] += count[i-1] 
    i = n-1
    while i>=0: 
        index = int(arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
#Radix Sort 
def radixSort(arr): 
    max1 = max(arr) 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10

#Count sort, works only with positive numbers
def countSort(tlist, k):
    count_list = [0]*(k)
    for n in tlist:
        count_list[n] = count_list[n] + 1
    i=0
    for n in range(len(count_list)):
        while count_list[n] > 0:
            tlist[i] = n
            i+=1
            count_list[n] -= 1