

def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<= pivot:

            i = i+1
            arr[i],arr[j] = arr[j],arr[i]


    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(arr)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    # partition(arr,0,5)
    quickSort(arr, 0, n - 1)
    # print("排序后的数组:")
    # for i in range(n):
    #     print("%d" % arr[i])