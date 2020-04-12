# Sort

#### 冒泡排序

思想：相邻的两个元素进行比较，每一轮的比较，将最大（最小）放在末尾（开头）的位置。

时间复杂度：O(n^2)

空间复杂度：O(1)

稳定的排序（排完序后相同元素的前后位置没有改变）







#### 选择排序

思想：在待排序元素中找出最大（最小）值的**索引**，遍历一遍后将找出的最大（最小）元素和末尾（开头）元素进行交换。

时间复杂度：O(n^2)

空间复杂度：O(1)

不稳定





#### 插入排序

思想：将元素在已排好序的部分进行依次比较插入（在插入排序过程中，将待排序部分可以分为已排好序和未排序两部分），找到插入的位置后，要将插入位置的后面（前面）的元素整体后移（前移）一个位置。

时间复杂度：O(n^2)

空间复杂度：O(1)

稳定





#### 希尔排序

思想：插入排序的扩展，但待排序数组很大时，插入排序性能就会受影响。

1. 首先，将数组分成N组，按照元素间隔进行分组，例如，第一次分组数为数组的长，以后每次分组数为上次的一般，当分组数为1时，就说明将整个数组看作一个分组，即分组完成。
2. 将分好的组，进行组内插入排序。

**难点**：如何在排序的同时，进行插入排序

时间复杂度：比O(n^2)要快，具体时间要根据待排序数组内元素的分布情况

在代码部分，将组数定义为**gap**，初始值为待排序的长度或者长度的一半，**注意** gap既是组数也是间隔。



#### 计数排序

思想：首先生成一个k大小的空间，k的取值为待排序元素的max-min；然后将待排序元素放入到额外生成的空间中对应的下标位置；最终待排序元素都放在了额外空间中，只要依次取出额外空间中每个位置中的元素，就得到最终的结果。

时间复杂度：O(N)




