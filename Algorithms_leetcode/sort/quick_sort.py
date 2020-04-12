"""
每一次pass，pivot大于左边的元素，小于右边的元素
"""

def quick_sort(list):
    if len(list) <=1:
        return list

    pivot = list[0]
    left = quick_sort([x for x in list[1:] if x < pivot])   # 从下表1开始，找出小于pivot的元素
    right = quick_sort([x for x in list[1:] if x > pivot])  # 从下表1开始，找出大于pivot的元素

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