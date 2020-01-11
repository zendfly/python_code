"""
插入排序（insertion_sort）
1、遍历时，将当前元素插入以排序好的部分
2、当前元素从以排好序部分的末端开始比较，直到找到合适的位置
3、插入到合适位置，并将合适位置之后的元素向后移动一位

属性：
    稳定（有相同元素时，排序完后，原本前面的元素还是在排在前面）
    O(1)空间复杂度
    O(n^2)时间复杂度
"""

def insertion_sort(arr):
    if arr is None:
        return None

    for i in range(1,len(arr)):     #默认0下标为以排好序部分
        key = arr[i]        #需要插入的元素
        j = i-1     #已排好序部分的末端
        #未比较完以排好序部分或者插入位置不对时
        while j >= 0 and key < arr[j]:      #j >= 0 表示已排好序部分；key < arr[j] 表示不是合适位置
            arr[j+1] = arr[j]       #向后移动一位
            j -= 1      #每进行一次比较，j向前移动一个
        arr[j+1] = key      #插入合适的位置
    return arr


if __name__ == '__main__':
    list = [6,5,4,3,2,1]
    result = insertion_sort(list)
    print(list)