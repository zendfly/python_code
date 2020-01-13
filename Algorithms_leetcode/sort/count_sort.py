"""
技数排序（count sort）
1、找出数组中的最大、最小值
2、设置一个大小 = 最大值-最小值+1 的额外数组counts
3、利用下标统计arr中每个数出现的位置，arr中元素对应counts中下标为 counts[arr]+1
4、释放统计结果

适用于：
    待排序列表中元素差值较小，重复元素较多
不足：当元素较多时，需要额外的空间较多
属性：
    不稳定
    O(n)时间复杂度
    O(K)空间复杂度
"""
def count_sort(arr):

    #寻找待排序列表中min、max值
    max_index,min_index = arr[0],arr[0]
    for i in arr:
        if i<min_index:min_index = i
        elif i>max_index:max_index = i

    nums = max_index-min_index+1        #待排序列表中元素区间
    counts = [0]*nums       #创建一个长度和待排序类别元素区间大小相同的集合
    for i in arr:
        counts[i-min_index] +=1         #使用下标进行统计，i-min_index为i对应的下标

    #进行重新排序
    pos = 0
    for i in range(nums):
        for j in range(counts[i]):
            arr[pos] = i+min_index
            pos +=1
    return arr



if __name__ == '__main__':
    arr = [10,1,3,4,2,8,11,4,67,3]
    print(count_sort(arr))