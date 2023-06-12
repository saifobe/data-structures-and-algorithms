def InsertionSort(input):
    for i in range(1, len(input)):
        value = input[i]
        j = i - 1
        while j >= 0 and value < input[j]:
            input[j + 1] = input[j]
            j = j - 1
        input[j + 1] = value

    return input