def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original array:", arr)

arr = quick_sort(arr)

print("Sorted array:", arr)
