# data-structures-and-algorithms


# Challenge Title
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
![code Challenge 02](./Untitled%20(2).jpg "reversArray")

## Approach & Efficiency
The array binary search algorithm is a search algorithm that works by repeatedly dividing the search interval in half. Given a sorted array arr of n elements and a target value key, the algorithm compares the target value with the middle element of the array. If the target value matches the middle element, the search is complete. Otherwise, if the target value is less than the middle element, the search continues on the lower half of the array. If the target value is greater than the middle element, the search continues on the upper half of the array. This process is repeated until the target value is found or the search interval is empty.

## Solution

``` python
def BinarySearch(arr,key):
    low = 0
    high = len(arr) -1

    while arr[low]<= key and key <= arr[high]:
        mid = (low + high) // 2
        
        if  key < arr[mid] :
            high = mid - 1 # high index = mid index -1
        elif key > arr[mid] :
            low = mid + 1  # low index = mid + 1
        elif arr[mid] == key:
            return mid
            
        
    return -1

arr1 = [10,11,12,14,15]

print(BinarySearch(arr1,14))


```

### Saif Obeidat