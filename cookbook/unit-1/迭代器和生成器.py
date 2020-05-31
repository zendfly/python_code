"""
interstor（迭代器）
    可以用作for循环
    使用next()函数返回下一个值，当到最后一个元素时，会抛出StopIteration异常，即说明没有下一个元素


"""

# 使用next()方法来进行迭代，遇StopIteration停止
def manual_iter():
    with open('cookbook','r') as f:
        try:
            while True:
                line = next(f)
                print(line)
        except StopIteration:
            pass

# 除了使用StopIteration异常外，可以使用None进行判断
def manual_iter_a():
    with open('cookbook','r') as f:
        while True:
            line = next(f)
            if line is None:
                break
            print(line)



