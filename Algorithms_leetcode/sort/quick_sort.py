"""

"""

def quick_sort(list):
    if len(list) <=1:
        return list

    pivot = list[0]
    left = quick_sort([x for x in list[1:] if x < pivot])
    right = quick_sort([x for x in list[1:] if x > pivot])

    return left + [pivot] + right

def quick_sort_a(list):

    left = []
    right = []
    pivot = list[0]
    for i in list[1:]:
        if i < pivot:
            left.append(i)
        else:right.append(i)
    return left+[pivot]+right

if __name__ == '__main__':
    list = [6,5,4,3,2,1]
    list1 = [3,5,2,7,8,3,2]
    # result = quick_sort_a(list)
    # print(result)
    pivot = list[0]
    print([x for x in list[1:] if x < pivot])