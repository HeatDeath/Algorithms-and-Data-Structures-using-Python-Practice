def position(alist, leftMark, rightMark):
    flag = alist[leftMark]
    j = leftMark
    for i in range(leftMark+1, rightMark+1):
        if alist[i] < flag:
            j += 1
            alist[j], alist[i] = alist[i], alist[j]

    alist[leftMark], alist[j] = alist[j], alist[leftMark]
    return j

def quickSort(alist, leftMark, rightMark):
    if leftMark >= rightMark:
        return
    mark = position(alist, leftMark, rightMark)
    quickSort(alist, leftMark, mark-1)
    quickSort(alist, mark+1, rightMark)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

quickSort(alist, 0, len(alist)-1)

print(alist)







