def quick_sort(arr, low, high):
    if low < high:
        print("Current Array State: ", arr)
        m = partition(arr, low, high)
        quick_sort(arr, low, m - 1)
        quick_sort(arr, m + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    print("\nPivot is: ", pivot)
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i+=1
        while i <= j and arr[j] > pivot:
            j -= 1

        if i <=j:
            arr[i], arr[j] = arr[j], arr[i]
            print("Swapped: ", arr)
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    print("Pivot Positioned: ", arr)
    return j


arr = [45, 67, 23, 89, 12, 90, 34]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("\nFinal Sorted Array:", arr)