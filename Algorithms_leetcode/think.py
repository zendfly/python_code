

gap = 10
length = 10

while gap>0:
    print('---------gap：%s-------'%(gap))
    for i in range(gap,length):     #gap分组数
        print('---------i：%s-------'%(i))
        for j in range(i,gap-1,-gap):
            pass
            # print(i)
            print(j)
    if gap == 2:
        gap = 1
    else:
        gap = gap//2