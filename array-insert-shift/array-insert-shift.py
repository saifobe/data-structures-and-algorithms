def insertShiftArray(arr, val):
    n = len(arr)
    mid = (n // 2) + (n % 2)   
    shifted = [None] * (n+1)   

    
    for i in range(mid):
        shifted[i] = arr[i]


    shifted[mid] = val

    
    for i in range(mid, n):
        shifted[i+1] = arr[i]

    return shifted

arr2 = [42,8,15,23,42]
val2 = 16
print(insertShiftArray(arr2, val2))

