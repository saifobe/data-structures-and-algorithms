def reverseArray(arr):
    
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr


my_arr = [1, 2, 3, 4, 5]
print(reverseArray(my_arr))

