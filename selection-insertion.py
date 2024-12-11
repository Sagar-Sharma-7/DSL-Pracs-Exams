from datetime import datetime

def selection_sort(arr):
    n = len(arr)
    print("\nSelection Sort: ")
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if(arr[j] < arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Iteration {i + 1}: {arr}")
    return arr

def insertion_sort(arr):
    n = len(arr)
    print("\nInsertion Sort: ")
    print(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
        print(f"Iteration {i}: {arr}")
    return arr

def main():
    marks = eval(input("Enter array of marks: "))
    marks2 = marks[:]
    start1 = datetime.now()
    final_arr1 = selection_sort(marks)
    print(final_arr1)
    end1 = datetime.now()
    print((end1.timestamp() * 1000 - start1.timestamp() * 1000), " ms")

    start2 = datetime.now()
    final_arr2 = insertion_sort(marks2)
    print(final_arr2)
    end2 = datetime.now()
    print((end2.timestamp() * 1000 - start2.timestamp() * 1000), " ms")
    
main()