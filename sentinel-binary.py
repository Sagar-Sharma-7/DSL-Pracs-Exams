# sentinel search

from datetime import datetime
def sentinel_search(arr, key):
    n = len(arr)
    last = arr[n-1]
    arr[n-1] = key

    i = 0
    while arr[i] != key:
        i += 1

    arr[n-1] = last
    if (i < n - 1) or (arr[n-1] == key):
        return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = low + (high-low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

def main():
    n = eval(input("Enter your list: "))
    key = int(input("Enter key: "))

    print("Using Sentinel Search")
    starttime1 = datetime.now()
    value = sentinel_search(n, key)
    if(value != -1):
        print("Found at ", value)
    else:
        print("Not found")
    endtime1 = datetime.now()
    print("\ntime taken: ")
    print((endtime1.timestamp() * 1000 - starttime1.timestamp() * 1000), " ms")

    print("Using Binary Search")
    starttime2 = datetime.now()
    value = binary_search(n, key)
    if(value != -1):
        print("Found at ", value)
    else:
        print("Not found")
    endtime2 = datetime.now()
    print("\ntime taken: ")
    print((endtime2.timestamp() * 1000 - starttime2.timestamp() * 1000), " ms")

main()