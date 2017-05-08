#交换不相邻的而元素以此对数组进行局部排序，并最终用插入排序将局部有序的数组排序
def shellSort(alist):
    h = 1
    while h < len(alist)/3:
        h = h*3 + 1

    while h >= 1:
        for i in range(h, len(alist)):
            for j in range(i, h-1, -h):
                if alist[j] < alist[j-h]:
                    alist[j], alist[j-h] = alist[j-h], alist[j]

        h = int(h/3)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

shellSort(alist)

print(alist)




