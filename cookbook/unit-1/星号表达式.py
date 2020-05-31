"""
星号表达式 - ‘*’，其作用可以分为三种：
    1、参数解包，作为函数的可变参数标志以及在特定语境下对可迭代对象进行解包以及参数传递
    2、用作赋值变量中的可变参数标志
    3、在非函数参数的其他特定语境中直接对可迭代对象进行解包操作
    总的来说，星号表达式主要作用是用于对可迭代对象进行解包

"""

'------------------------示例（1）----------------------------'
# 当一个参数前面加上*时，表示这个参数是一个可变参数，其中：
# 一颗星时---*，表示这个参数是可变的位置参数，并以元组的形式将外部的多个位置参数返回给参数变量
# 两颗星时---**，表示这个参数是可变的关键词参数，以字典的形式将外部的多个关键词参数返回个参数变量
def f1(a,*b,**c):
    print(a)
    print(b)
    print(c)

f1(1,2,(3,4),k1=1,k2=3,k3=4)

# output
# 1
# (2, (3, 4))
# {'k1': 1, 'k2': 3, 'k3': 4}

# *时，是可变的位置参数，返回元组；**时，是可变的关键字参数，返回字典。

'------------------------示例（2）----------------------------'
# 将一个可迭代对象作为参数传递给一个函数时，在这种语境下，可以直接利用'*iterable'语法对可迭代对象进行解包，并把解包后的内容传递函数
def f2(a,b,c):
    print(a)
    print(b)
    print(c)

f2(*(1,2,3))
f2(*[4,5,6])

# output
# 1
# 2
# 3
# 4
# 5
# 6

# 函数中有可变的位置参数，并使用*iterable的形式进行参数传递，可以避免出现参数个数不匹配的异常
def f3(a,*b):
    print(a)
    print(b)

f3(*(1,2,3,4,5,6))
f3(*[2,3,4,5,6,7])

# output
# 1
# (2, 3, 4, 5, 6)
# 2
# (3, 4, 5, 6, 7)

# 解包后的元素与函数位置参数的个数不相等，会抛出异常，一般情况下，不建议在不可变参数的函数中使用这种传参

'------------------------示例（3）----------------------------'
# 在赋值语句中作为可变变量标志
a,*b = [1,2,3,4,5]
*c,d = range(10,15)

print(a)
print(b)
print(c)
print(d)

# output
# 1
# [2, 3, 4, 5]
# [10, 11, 12, 13]      type:list
# 14

# 当我们想要对一个可迭代对象进行拆分，并赋值给变量时，我们可以用星号标记某个变量，这个变量表示可变变量，意思是这个变量的内容是可变的
# 其内容根据其他变量的个数决定。其原理就是优先赋值给确定的变量，将剩余的变量赋值给可变变量，实际上，可变变量的内容就是可迭代对象剩下
# 内容解包后得到的内容，并以List的形式进行返回


'------------------------示例（4）----------------------------'
# 从3.5版本开始，python对星号增加了新的适用场景，可以在元组(tuple)、列表(list)、字典(dir)和集合(set)内部进行对可迭代参数直接解包。
# 只有在上述四种场景下才可以对可迭代参数进行解包

a = *range(4),      # 如果 a = range(4)，其type(a) = range，不在上述四种情况下，但加上 ',' 后就是一个tuple
b = *range(3),3     # 和 a 同理
c = [*range(3)]
d = {*range(3)}
e = {**{'y':1}}

print(a)
print(type(a))
print(b)
print(c)
print(d)
print(e)

# output
# (0, 1, 2, 3)
# <class 'tuple'>
# (0, 1, 2, 3)
# [0, 1, 2]
# {0, 1, 2}
# {'y': 1}