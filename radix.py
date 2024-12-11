def counting(arr, place):
    n = len(arr)
    result = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // place) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n - 1
    while(i >= 0):
        index = (arr[i] // place) % 10
        result[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = result[i]

def radix(arr):
    max_element = max(arr)
    place = 1
    while max_element // place > 0:
        counting(arr, place)
        place *= 10
    print(arr)

arr = [170,45,75,90,802,24,1]
radix(arr)