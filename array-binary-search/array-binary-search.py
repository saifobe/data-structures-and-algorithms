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

        
     