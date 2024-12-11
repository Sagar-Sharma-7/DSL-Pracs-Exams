def bubble(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if(not swapped):
            break
        print(f"Iteration {i+1}: {arr}")
    
    return arr


def shell_sort(arr):
    n = len(arr)
    gap = n//2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print(f"\nIteration: {arr}")
        gap //=2
    return arr
arr = [2,25,6,1,0,8,3]
arr2 = [2,25,6,1,0,8,3]
print(bubble(arr))
print(shell_sort(arr2))