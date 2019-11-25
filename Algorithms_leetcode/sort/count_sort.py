#找出数组中的最大、最小值
#设置一个大小 = 最大值-最小值+1 的额外数组counts
#利用下标统计arr中每个数出现的位置，arr中元素对应counts中下标为 counts[arr]+1
#释放统计结果
def count_sort(arr):

    max_index,min_index = arr[0],arr[0]
    for i in arr:
        if i<min_index:min_index = i
        elif i>max_index:max_index = i

    nums = max_index-min_index+1
    counts = [0]*nums
    for i in arr:
        counts[i-min_index] +=1
    # print(counts)
    pos = 0
    for i in range(nums):
        for j in range(counts[i]):      #for i in range(0) print(i)为空
            arr[pos] = i+min_index
            pos +=1
    return arr

#时间复杂度为O(n)

if __name__ == '__main__':
    arr = [10,1,3,4,2,8,11,4,67,3]
    print(count_sort(arr))