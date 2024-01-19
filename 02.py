def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_border = None
 
    while low <= high:
        mid = (high + low) // 2
        iterations += 1

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] >= x:
            high = mid - 1
            upper_border = arr[mid]

    if upper_border == None:
        result = f"The required value is outside the array. The largest value of the array: {arr[-1]}."
    else:
        result = (iterations, upper_border)
    return result
