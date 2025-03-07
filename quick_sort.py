# https://www.geeksforgeeks.org/problems/quick-sort/1
def partition(arr, low, high):
    i = low - 1
    for j in range(low, high):
        if arr[j] < arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


arr = [4, 1, 3, 9, 7]
print(quicksort(arr, 0, len(arr) - 1))
