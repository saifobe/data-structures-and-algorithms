def Mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        Mergesort(left)
        Mergesort(right)
        
        marge(left, right, arr)
    return arr
def marge(left, right, arr):
    i = 0
    j = 0
    k = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i] 
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            
        k += 1
        
    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]
        
    return arr

if __name__ == "__main__":
    arr = [20,18,12,8,5,-2]
    Mergesort(arr)
    print(arr)