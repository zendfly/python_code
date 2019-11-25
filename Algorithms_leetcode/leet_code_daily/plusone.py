
def plusone(digits):
    i = -1
    digits[i] = digits[i]+1

    while digits[i] == 10:
        if i != -len(digits):
            digits[i] = 0
            digits[i-1] = digits[i-1]+1
            i -=1
        else:
            if digits[i] == 10:
                digits[0] = 1
                digits.append(0)
    return digits


def plusone_a(digtis):
    digtis = digtis[::-1]
    index = 0
    n = len(digtis)
    c = 1
    while c == 1 and index < n:
        t = (digtis[index] + c) % 10
        c = (digtis[index] + c) // 10
        digtis[index] = t
        index += 1
    if c == 1:
        digtis.append(1)
    return digtis[::-1]

if __name__ == '__main__':
    n = [9]
    print(plusone(n))

