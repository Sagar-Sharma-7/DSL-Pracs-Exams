def fibonacci(arr, k):
    n = len(arr)
    b = 0
    a = 1
    f = b + a
    
    while(f < n):
        b = a
        a = f
        f = a + b
    
    offset = -1
    print(f"{'f':<7}{'a':<7}{'b':<7}{'offset':<10}{'i':<10}")
    print("-" * 40)

    while(f > 1):
        i = min(offset + b, n - 1)
        print(f"{f:<7}{a:<7}{b:<7}{offset:<10}{i:<10}")

        if(arr[i] < k):
            f = a
            a = b
            b = f - a
            offset = i
        elif(arr[i] > k):
            f = b
            a = a - b
            b = f - a
        else:
            return i
        
    if(a and offset + 1 < n and arr[offset + 1] == k):
        print("from last")
        return offset + 1
    
    return -1

def main():
    arr = [1, 3, 5, 7, 9]  # The array
    k = 9                  # The key (last element)
    result = fibonacci(arr, k)
    print("result: ", result)

main()