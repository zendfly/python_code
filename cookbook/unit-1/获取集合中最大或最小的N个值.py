# -*- coding:utf-8 -*-
# @Time: 22:40
# @Author:zendfly


import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3,nums))       # 取最大的3个值
print(heapq.nsmallest(3,nums))      # 取最小的3个值


# heapq在进行前N个值查找时，首先会对dateset进行堆（heap）排序
# 堆数据结构中，最重要是 heap[0]永远是最小的
# 使用heapq.heappop()将第一个元素弹出，然后用下一个最小的元素取代被弹出的元素
heap = list(nums)
heapq.heapify(heap)
print(heap)


# 如果想要取最小的三个元素
print(heapq.heappop(heap))
print(heapq.heappop(heap),
    heapq.heappop(heap))


# max,min比nlargest,nsmallest要快一些，并且sorted(item)[:N),sorted(item)[-N:]的切片操作也较快
# 但当N和len(item)教接近时，heapq更合适