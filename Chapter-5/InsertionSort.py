def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        # 从位置alist[index-1]开始向左遍历到alist[0]
        for j in range(index - 1, -1, -1):
            if currentvalue < alist[j]:  # 若遇到大于a[i]的元素，将其右移(此时a[i]"悬空")
                alist[j + 1] = alist[j]
                position -= 1  # 位置标记左移一位

        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)