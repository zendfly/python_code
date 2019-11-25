#两个链表合并，循环结束条件是 L1和L2都循环到最后一个节点


#失败
def addTwoNumbers(l1,l2):

    min_len ,max_len = min(len(l1),len(l2)),max(len(l1),len(l2))
    out_list = [0] * int(max_len+1)
    i = 0
    while i < max_len:
        if l1[i] is None:
            l1[i] =0
        if i > len(l2):
            l2[i] =0
        index_i_sum = l1[i] + l2[i]
        index_i_1, index_i_2 = index_i_sum // 10, index_i_sum % 10  # index_i_1取整，index_i_2求余

        if index_i_1 == 1:
            out_list[i] += index_i_2
            out_list[i + 1] += 1
        else:
            out_list[i] = index_i_sum
        i += 1
    if out_list[-1] == 0:
        out_list.pop()

    return out_list

if __name__ == '__main__':
    l1 = [1,3,9]
    l2 = [3,2,4,1]
    print(addTwoNumbers(l1,l2))





