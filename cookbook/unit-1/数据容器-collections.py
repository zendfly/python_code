# -*- coding:utf-8 -*-
# @Time: 22:40
# @Author:zendfly

import collections
"""
collections:这个模块实现了特定目标的容器，以提供python标准内建容器dict、list、set和tuple的替代选择

nametuple:创建命名元组子类的工厂函数
duque:类似列表的容器，实现了在两端快速添加(append)和弹出(pop)
ChainMap:类似字典(dict)的容器类，将多个映射集合到一个视图里面
Counter:字典的子类，提供了可哈希对象的计数功能
OrderedDict:字典的子类，保存了他们被添加的顺序
"""



# Counter() 用于计数可哈希对象，它是一个集合，元素像字典键(key)一样存储
# 计数可以是任何整数值，包括0和负数
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)
# printout:Counter({'blue': 3, 'red': 2, 'green': 1})

c = collections.Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(c['yellow'])
# printout:0
# 如果引用的键没有任何记录，就返回一个0


